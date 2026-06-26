def bubble_sort(list_of_numbers):

    
    for i in list_of_numbers:
        for num in range(len(list_of_numbers[-1]), -1, -1):
            current = list_of_numbers[num]
            next_number = list_of_numbers[num - 1]

            print(f"Num:{num}, current number:{current}, number to compare:{next_number}")

            if current > next_number:             
                list_of_numbers[num + 1] = current
                print(f"Moving {current} element to {next_number} position")
                list_of_numbers[num] = next_number
            else:
                False


my_list = [11, 33, 0, -2, -100, 3, 34]
bubble_sort(my_list)
print(my_list)
