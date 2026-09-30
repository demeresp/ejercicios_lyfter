def bubble_sort(list_of_numbers):

    if not isinstance(list_of_numbers, list):
        raise TypeError("Input is not a list")


    for i in range(len(list_of_numbers)):
        swapped = False 
        for num in range(0, len(list_of_numbers)- 1):
            current = list_of_numbers[num]
            next_number = list_of_numbers[num + 1]

            print(f"Num:{num}, current number:{current}, number to compare:{next_number}")
            
            if current > next_number:
                swapped = True           
                list_of_numbers[num + 1] = current
                print(f"Moving {current} element to {next_number} position")
                list_of_numbers[num] = next_number
                
        if not swapped:
            break



my_list = [9, 2, -4, 87, -31, 0, 1]
bubble_sort(my_list)
print(my_list)
