def lower_upper(word1, word2, word3):
    result = []
    for word in [word1, word2, word3]:
        upper = sum(1 for i in word if i.isupper())
        lower = sum(1 for i in word if i.islower())
        result.append(f"'{word}' tiene: {upper} mayusculas y {lower} minusculas ")
    return "\n".join(result)

print(lower_upper("El bicho", "Critiano", "SIIUuuu"))