numbers = []

while len(numbers) < 3:
    number = (input("Introduzca su numero:",))
    numbers.append(int(number))

largest_number = int(number[0])  

for number in numbers:
    if number > largest_number:
        largest_number = number
print("El numero mayor es:", largest_number)




