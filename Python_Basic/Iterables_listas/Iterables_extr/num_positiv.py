import random
random_numbers = [random.randint(-10, 10) for num in range(1,11)]
print("Lista generada:", random_numbers)

positives = len([num for num in random_numbers if num > 0])
print(f"Hay {positives} numero positivos")
        