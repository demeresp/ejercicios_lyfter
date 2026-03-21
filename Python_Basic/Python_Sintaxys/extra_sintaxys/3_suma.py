number = int(input("Digite su numero:",))
my_list = list(range(1, number + 1))
suma = sum(my_list)
print(f"{" + ".join(map(str, my_list))} = {(suma)}")