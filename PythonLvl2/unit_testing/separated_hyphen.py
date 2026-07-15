def my_wordzz(definition1, definition2, definition3):
    word = [definition1, definition2, definition3]
    word.sort()#sort para ordenar las palabras
    return " - ".join(word) 

print(my_wordzz("This", "is", "JOHN CENA!"))
    