def amount_carac():

    count = 0
    word = (input("Introduzca su palabra:",))
    caracther = input("Introduzca el caracter a contar:",)
    for letter in word:
        if letter == caracther:
            count = count + 1
        
    print(f"La letra {caracther} esta {count} veces en {word}")


amount_carac()



