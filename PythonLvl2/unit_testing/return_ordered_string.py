def turn_word(word):
    if not isinstance(word, str):
        raise TypeError("Input must be a string")

    return ''.join(reversed(word))

my_word = "This is a test string"
result = turn_word(my_word)
print(result)
