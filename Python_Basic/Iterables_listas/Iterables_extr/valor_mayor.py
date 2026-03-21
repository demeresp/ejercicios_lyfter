average = 10
import random
numbers = [random.randint(1,20) for num in range(1,11)]
highers = []

for num in numbers:
    if num > average:
        highers.append(num)

print(f"En la lista {numbers} los arriba del promedio son: {highers}")

if len(highers) > 0:
    average_highers = sum(highers) / len(highers)
    print("El promedio de los mayores es:", average_highers)
else:
    print("No hay numeros mayores al promedio")