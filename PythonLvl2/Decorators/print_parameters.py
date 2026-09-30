def printer_parameters(fun):
    def wrapper(*args): #calquier cantidad de argumetos
        print("Parameters:", args)
        result = fun(*args)
        print("Result:", result)
        return result
    return wrapper


@printer_parameters
def plus(p1, p2):
    return p1 + p2


plus(50, 22)