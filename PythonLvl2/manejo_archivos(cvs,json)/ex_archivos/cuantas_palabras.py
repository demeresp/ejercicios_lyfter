def file_counter(route):
    with open(route, 'r', encoding='utf-8') as file:
        text = file.read()
        amount_words = len(text.split())
        print("La cantidad de palabras en el archivo es", amount_words)
        

file_counter(r"C:\Users\demer\OneDrive\Desktop\Lyfter\Programs\archivos\ex_archivos\fixed_text.txt")