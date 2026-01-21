price = int(input("Cual es el precio del producto:",))
discount = 0

if price < 100:
    discount = price * 0.02
else: 
    discount = price * 0.10
    final_price = price - discount
print("El precio final es:", final_price)