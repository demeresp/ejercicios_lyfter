def amount_words():
    while True:
        words = [input(f"Palabra {i+1}: ") for i in range(0,4)] # comprehension list, pide 4 veces una palabra input, for i in range(0,4) y f"Palabra {i+1}: " pide y enumera# 
        if "" in words:
            print("Hacen falta elementos")
            continue 
        elif any(not word.isalpha() for word in words): 
            print("Solo puede escribir palabras y sin espacios ni numeros!")
            continue
        return words


def comparation():
    valid_words = []
    while True:
        my_words = amount_words()
        try:
            minimun_letters = int(input("Ingrese el numero de letras a buscar:", ))
        except ValueError as error:
            print("Debe digitar un numero!")
            continue
        for i in my_words:
            if len(i) >= minimun_letters:
                valid_words.append(i)
        return valid_words


def main():
    print("Bienvenido!")
    true_words = comparation()
    print(f"Las palabras validas son:, {true_words}")


main()