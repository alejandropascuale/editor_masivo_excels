
current_path = input("Ingrese la ruta donde quiere modificar los archivos: ")
list_files = []
for i, file in list_files:
    file_name = input("Ingrese nombre del archivo (sin extension). Si ya finalizo presione N").upper()
    if file_name != "N":
        list_files.append(f"{current_path}/{file_name}.xlsx")
    
print(list_files)