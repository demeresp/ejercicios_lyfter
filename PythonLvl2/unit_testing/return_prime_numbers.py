def my_numbers():
    primes = []                       
    for number in range(2, 101):
        prime = True                  
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0: 
                prime = False       
                break                  
        if prime:                   
            primes.append(number)
    return primes

print(my_numbers())
