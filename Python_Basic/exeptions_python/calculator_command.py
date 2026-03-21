def select_operation():
    while True:
        menu = (input("""Que operacion desea realizar? 
                        1.Suma, 2.Resta, 3.Multiplicacion, 4.Dividir, 5.Borrar:""", )).strip()
        try:
            selection = int(menu)
            if selection in [1,2,3,4,5]:
                return selection
            else: print("Debe seleccionar una opcion entre 1-5")
        except ValueError as error:
            print(f"{error} Debe digitar un numero")


def select_number():
    while True:
        op_number = (input("Ingrese el numero que desea operar:",))
        try:
            return int(op_number)
        except ValueError as nonumber:
            print(f"{nonumber} no es un numero! Debe digitar un numero")


def the_sum(num):
    print("Estaremos sumando...")
    sum_result = num + select_number()
    return sum_result


def the_rest(num):
    print("Estaremos restando...")
    rest_result = num - select_number()
    return rest_result


def the_multp(num):
    print("Estaremos multiplicando...")
    multp_result = num * select_number()
    return multp_result


def the_division(num):
    print("Estaremos dividiendo...")
    while True:
        try:
            division_result = num / select_number()
            return division_result
        except:
            ZeroDivisionError
        print("No se puede dividir por zero")
        continue


def main(initial_number = 10):
    while True:
        print("Bienvenido al programa ultra mejorado o empeorado :c!")
        print("El numero a operar es:", initial_number)
        choice_in_menu = select_operation()
        if choice_in_menu == 1:
            result = the_sum(initial_number)
        elif choice_in_menu == 2:
            result = the_rest(initial_number)
        elif choice_in_menu == 3:
            result = the_multp(initial_number)
        elif choice_in_menu == 4:
            result = the_division(initial_number)
        elif choice_in_menu == 5:
            try:
                del result
            except: UnboundLocalError
            print("Aun no hay un resultado para borrar")
            continue
        print("El resultado es:", result)
        initial_number = result

main()

