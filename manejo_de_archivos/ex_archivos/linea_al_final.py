def file_to_write():
    print("Buenas ;)")
    text = input("Introduzca un textillo:",)
    
    route = r"C:\Users\demer\OneDrive\Desktop\Lyfter\Programs\archivos\ex_archivos\texto_iterado.txt"
    try:
        with open(route, 'a', encoding="utf-8") as file:
            file.write(text)
    except: FileNotFoundError ("Wao, ese archivo no esta, pero ya le hacemos uno..")
    with open(route, 'a', encoding='utf-8') as file:
        file.write('\n' + text)


file_to_write()
