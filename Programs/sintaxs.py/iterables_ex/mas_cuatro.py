words = []
four_words = []

while len(words) < 4:
    word = input("Escriba su palabra:",)
    words.append(word)
for word in words:
    if len(word) > 3:
        four_words.append(word)
print(f"De la lista {words} las palabras con +4 letras son: {four_words}")
