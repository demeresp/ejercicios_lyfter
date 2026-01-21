number = int(input("Ingrese el numero a multiplicar:",))
multipliers = list(range(1,13))

for num in range(1,13):
    result = number * num
    print(f"{number} * {num} = {result}")

