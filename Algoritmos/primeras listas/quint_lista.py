numbers = []
while len(numbers) < 10:
    number = int(input("Ingrese el numero:",))
    numbers.append(number)
print(f"Los numeros son {"-".join((map(str, numbers)))} y el numero mayor es {max(numbers)}") ##comprh list##