# archivo: mi_programa.py

def pedir_edad():                              # ← Definimos una función que se llama pedir_edad
    while True:                                # ← Bucle infinito hasta que meta un número bueno
        try:                                   # ← Intentamos hacer esto...
            edad = int(input("¿Cuántos años tienes? "))   # ← Pedimos número
            if edad < 0:                       # ← Si mete edad negativa...
                raise ValueError("La edad no puede ser negativa, tío")  # ← lanzamos error nosotros mismos
            else: return edad                        # ← Si todo bien, devolvemos la edad y salimos de la función
        except ValueError as e:                # ← Si mete letras o el error que lanzamos arriba...
            print(f"Error: {e}. Inténtalo otra vez.")   # ← le decimos que la cague y vuelve a empezar

def saludar(nombre, edad):                     # ← Otra función simple
    print(f"Hola {nombre}, tienes {edad} años, ¡qué viejo estás ya!")

def main():                                    # ← Aquí está el cerebro del programa
    print("=== Bienvenido al programita ===")
    nombre = input("¿Cómo te llamas? ")
    edad = pedir_edad()                        # ← Llamamos a la función pedir_edad()
    saludar(nombre, edad)                      # ← Llamamos a la función saludar()
    print("¡Adiós, crack!")

# Y ahora viene la parte que te explota la cabeza...
if __name__ == "__main__":
    main()