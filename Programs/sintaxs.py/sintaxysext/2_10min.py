seconds = int(input("Tiempo en segundos:",))
ten_minutes = 600

if seconds == ten_minutes:
    print("El tiempo es igual")
elif seconds > ten_minutes:
    print("El tiempo es mayor")
else:
    missing_time = ten_minutes - seconds
    print("El tiempo faltante es:", missing_time)