def my_numbers(plus):#plus numero ingresado por el usuario
    if not isinstance(plus, (int, float)): 
        raise TypeError("Object is not a list")
    
    plus = int(plus)

    if plus < 0:
       raise TypeError("Negative numbers are not allowed")
    
    plus = list(range(1, plus + 1)) #range para crear una lista de números desde 1 hasta el número ingresado y +1 para incluir el número ingresado en la lista
    return sum(plus) # retorna la suma de los números en la lista

print ("result is:", my_numbers(33))