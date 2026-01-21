def word_and_vowels():
    vowels = ["a","e","i","o","u"]
    count = 0
    while True:
        word = input("Ingrese la palabra a contar:",)
        for letter in word:
            if letter not in vowels:
                continue
            if letter in vowels:
                count = count + 1
        print(f"La palabra {word} contiene: {count} vocales")

word_and_vowels()
