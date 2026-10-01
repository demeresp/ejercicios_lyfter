def file_reader(route):
    with open(route, 'r', encoding="utf-8") as file:
        text = file.read()
        modified_text = text.upper()
        return modified_text
    

def file_saver(new_file):
    with open(new_file, 'w', encoding="utf-8") as new:
        new.write(file_reader(r"C:\Users\demer\OneDrive\Desktop\Lyfter\Programs\archivos\ex_archivos\texto_iterado.txt"))


file_saver(r"C:\Users\demer\OneDrive\Desktop\Lyfter\Programs\archivos\ex_archivos\text_cap.txt") 