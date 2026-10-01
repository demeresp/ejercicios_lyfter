def file_reader(route):
    with open(route, 'r', encoding="utf-8") as file:
        readed_text = file.read()
        text_to_conv = readed_text.replace("\n", " ").strip()
        return text_to_conv


def file_saver(new_route):
    with open(new_route, 'w', encoding="utf-8") as new:
        new.write(file_reader(r"C:\Users\demer\OneDrive\Desktop\Lyfter\Programs\archivos\ex_archivos\texto_iterado.txt"))

def main():
    file_saver(r"C:\Users\demer\OneDrive\Desktop\Lyfter\Programs\archivos\ex_archivos\fixed_text.txt")


main()
