def sum_of_elements():
    elements = [input(f"Introduzca el signo convertir:" ,) for _ in range(5)]
    numbers_to_sum = []
    while True:
        for variable in elements:
            try:
                my_floats = float(variable)
                print(f"El elemento {variable} fue sumado correctamente")
                numbers_to_sum.append(my_floats)
                continue
            except:
                ValueError 
            print("Elemento invalido:", {variable})
            continue
        result = sum(numbers_to_sum)
        print("EL resultado es:", result)
        break


sum_of_elements()