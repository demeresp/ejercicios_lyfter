import random
numbers = list(range(1,11))
num_secret = random.choice(numbers)

new_num = int(input("Introduzca el numero secreto:",))

while new_num != num_secret:
    print("Incorrecto, por favor intente de nuevo")
    new_num = int(input("Introduzca el numero secreto:",))
print("El numero", new_num, "es correcto",)



