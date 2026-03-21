def name():
    while True:
        user_name = (input("Ingrese su nombre:",)).strip()
        if user_name.isdigit():
            raise ValueError("Debe haber solo letras en el nombre")
        elif str(user_name):
            return user_name


def age():
    while True:
        user_age = (input("Ingrese su edad:",))
        try:
            int(user_age)
        except ValueError:
            print("Solo numeros aca!")
            continue
        return user_age


def main():
    print("Bienvenido al programita!")
    the_name = name()
    the_age = age()
    print(f"Hola {the_name}, su edad es {the_age}")


main()
