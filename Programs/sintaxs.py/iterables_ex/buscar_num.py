numbers = []

while len(numbers) < 7:
    number_compare = int(input("Cree la lista de numeros:", ))
    numbers.append(number_compare)
number = int(input("Digite el numero a comparar:", ))

print(f"El numero, {number} aparece: {numbers.count(number)}, veces")

