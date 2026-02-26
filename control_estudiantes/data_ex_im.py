import csv
import os



def file_reader(route):
    with open(route, 'r', encoding="utf-8") as file:
        try:
            reader = csv.DictReader(file)
            return list(reader)
        except FileNotFoundError:
            print("The route provided is invalid")



def student_saver(file, student):
    try:
        with open(file, 'a', encoding="utf-8") as f:
            columns = ["grade", "name", "spanish", "english", "history", "sciences"]
            content = csv.DictWriter(f, fieldnames=columns)
            content.writerow(student)
    except FileNotFoundError as error:
        print("The file indicated does not exist")
    return content



def file_saver(content, route):
    try:
        with open(route, "w", encoding="utf-8") as file:
            content = csv.DictWriter(file, fieldnames=content.fieldnames) #content.ffieldnames para que sepa que columnas va a escribir, si no se lo indico no va a escribir nada, es como un formato para el csv
            content.writeheader()
            content.writerows(content)
    except FileNotFoundError as oops:
        print("Looks like this file is not foundable right now...")
    return content


def route_validator(route=None):
    route = input("Please, provide the route of the file you want to work with:").strip().strip('"').strip("'")##strip para eliminar espacios al inicio y al final, strip('"') para eliminar comillas dobles, strip("'") para eliminar comillas simples, así el usuario puede ingresar la ruta con o sin comillas y no va a afectar el funcionamiento del programa
    if not route.lower().endswith('.csv'): #endswith para verificar que la ruta termine con .csv o pa lo que ocupe kk
        print("The file provided is not a csv file, please provide a valid route")
        return None
    elif ':' not in route and '\\' not in route and '/' not in route: #para verificar que la ruta tenga al menos una carpeta, si no tiene ninguna carpeta es una ruta inválida, esto es para evitar que el usuario ingrese solo el nombre del archivo sin especificar la ruta, lo cual podría causar problemas si hay varios archivos con el mismo nombre en diferentes carpetas
        print("The route provided is invalid, please make sure you are not skipping any caracter of the route")
        return None
    elif not os.path.isfile(route): #os.path.isfile para verificar que la ruta proporcionada corresponde a un archivo existente
        print("The route provided does not correspond to an existing file, please provide a valid route")
        return None
    try:
        with open(route, 'r', encoding="utf-8") as file:
            return route
    except (FileNotFoundError, PermissionError, OSError, IsADirectoryError, UnicodeDecodeError) as invalid: #1.Archivo no encontrado, 2.Permiso denegado, 3.Caracteres invalidos de ruta, 4.El archivo es un directorio, no carpeta, 5. El archivo no se puede leer con ese encoding el 'utf-8' pues! 
        print("The route provided is invalid")
        return False