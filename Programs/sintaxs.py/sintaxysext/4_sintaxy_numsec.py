numbers = []

while len(numbers) < 3:
    number = int(input("Digite un numero:",))
    numbers.append(number)

if 30 in (numbers):
        print("El numero ingresado es correcto:", 30)
elif (sum(numbers)) == 30:
        print(f"La suma de los numeros es correcta: {numbers[0]} + {numbers[1]} + {numbers[2]} = 30")
else:
    print("La suma de los numeros es incorrecta!")
        
