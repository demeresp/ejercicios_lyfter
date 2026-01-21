# Pedir nombre, apellido y edad #

name = input("Introduzca su nombre:", )
last_name = input("Introduzca su apellido:", )
age = int(input("Introduzca su edad:", ))


if age <= 3:
    print (f"{name} {last_name} es un bebe")
elif age <= 9: 
    print (f"{name} {last_name} es un nino")
elif age <= 13:
    print (f"{name} {last_name} es un preadolescente")
elif age <= 18:
    print (f"{name} {last_name} es un adolescente")
elif age <= 30:
    print (f"{name} {last_name} es un adulto joven")
elif age <= 59:
    print (f"{name} {last_name} es un adulto")
else:   
    print (f"{name} {last_name} es un adulto mayor")
