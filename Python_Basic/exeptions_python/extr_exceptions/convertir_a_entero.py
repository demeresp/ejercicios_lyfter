def words_register():
        words = [input(f"Introduzca la palabra a convertir:",) for _ in range(5)] ##Comprh list##
        while True:
            for element in words:
                try:
                    words_converted = int(element)
                    print(f"{element}, fue convertido a {words_converted}")
                except ValueError:
                    print(f"No se pudo convertir el elemento, '{element}' ")
                    continue
            return words_converted
        

words_register()