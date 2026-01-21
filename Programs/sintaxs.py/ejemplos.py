# Primer ejemplo #

mensaje = input(str("Introducir su mensaje:" ,))
respuesta = input(str("Introduzca su respuesta:" ,))

print(f"""{mensaje} 
      
{respuesta}""")

# Segundo ejemplo #

color_de_piso = (input("En que color de piso estaciono?:",))
numero_parqueo = int(input("Cual era el numero de lote?:", ))
numero_parqueo = str(numero_parqueo)

localizacion_de_vehiculo = color_de_piso + " " + numero_parqueo

print("Su vehiculo se encuentra en:", localizacion_de_vehiculo)


# Tercer ejemplo # 

numero_boleto = int(input("Introduzca su numero de boleto:", ))
nombre_de_fila = (input("Introduzca el nombre de la fila:", ))
numero_boleto = str(numero_boleto)

localizacion = numero_boleto + " " + nombre_de_fila

print("Su localizacion es en:", localizacion)

# Cuarto ejemplo #

asientos_vacios = [i for i in range(30)]

asientos_comprados = [i for i in range(25)]

asientos_totales = len(asientos_vacios) + len(asientos_comprados)
print("Total de asientos:", asientos_totales)

# Quinto ejemplo #

equipos = ["equipo verde", "equipo rojo", "equipo azul"]
ultimo_equipo = input("Cual es el ultimo equipo:?", )

equipos.append(ultimo_equipo)
lista_final = equipos

print(lista_final)

# Sexto ejemplo #

precio_de_papas = float(input("Cual es el precio de las papas:",))
precio_hamburguesa = int(input("Cual es el precio de la hamburguesa:",))

precio_de_papas = int(precio_de_papas)

precio_combo = precio_de_papas + precio_hamburguesa
print("El precio del combo es:", precio_combo)

# Septimo ejemplo #

1 = True
2 = False

resultado = 1 + 2











