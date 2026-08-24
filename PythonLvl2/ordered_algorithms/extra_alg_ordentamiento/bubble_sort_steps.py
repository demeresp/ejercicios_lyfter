def bubble_sort(list_of_numbers):
    iterations = 0    
    swaps = 0         

    for i in range(len(list_of_numbers) - 1):
        swapped = False
        iterations += 1    
        
        for num in range(0, len(list_of_numbers) - 1):
            current = list_of_numbers[num]
            next_number = list_of_numbers[num + 1]

            if current > next_number:
                swapped = True
                swaps += 1    # cada swap suma 1
                list_of_numbers[num] = next_number
                list_of_numbers[num + 1] = current

        if not swapped:
            break

    print(f"Total iterations: {iterations}, total swaps: {swaps}")


mylist = [4, 3, -3, 0, 55, -1, 22]
bubble_sort(mylist)
print(mylist)