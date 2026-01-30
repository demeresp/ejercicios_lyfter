def my_wordzz(definition1, definition2, definition3):
    word = [definition1, definition2, definition3]
    word.sort()
    return " - ".join(word) 

print(my_wordzz("Veamo", "Si es", "Uste"))
