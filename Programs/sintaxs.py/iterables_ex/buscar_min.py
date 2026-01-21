import random
numbers = [random.randint(1,10) for i in range (11)]

minor = numbers[0]
for i in numbers:
    if i < minor:
        minor = i
print(f"El menor de la lista {numbers} es {minor}")