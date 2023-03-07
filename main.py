from openpyxl import load_workbook
from datetime import date
import warnings
warnings.simplefilter("ignore")

current_path = input("Ingrese la ruta donde quiere modificar los archivos: ")
list_files = []

n = 1
while n < 1000000:
    file_name = input("Ingrese nombre del archivo (sin extension). Si ya finalizo presione N: ")
    if file_name.upper() != "N":
        list_files.append(f"{current_path}/{file_name}.xlsx")
    else:
        break
    
print(list_files)

def change_wb (path, sheet, cell, text):
    t_date = date.today()
    format_date = f"{t_date.day}/{t_date.month}/{t_date.year}"
    wb = load_workbook(path)
    wb_sheet = wb[sheet]
    wb_sheet[cell] = text
    # Agregar otro while en el que se pregunta por si hay mas cambios para hacer
    wb_sheet["B27"] = f"Ultima actualización: {format_date} por Alejandro Pascuale"
    wb.save(path)
    wb.close

for file in list_files:
    change_wb(file, "Resumen", "C6", "10mm x 236mm x 1835mm")