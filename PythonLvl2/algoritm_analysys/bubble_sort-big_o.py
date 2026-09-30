def bubble_sort(list_of_numbers):

    #0(n^2) - Algorithm complexity
    for i in range(len(list_of_numbers)): #0(n) 
        swapped = False #0(1)
        for num in range(0, len(list_of_numbers)- 1): #0(n)
            current = list_of_numbers[num] #0(1)
            next_number = list_of_numbers[num + 1] #0(1)

            print(f"Num:{num}, current number:{current}, number to compare:{next_number}") #0(1)
            
            if current > next_number: #0(1)
                swapped = True #0(1)           
                list_of_numbers[num + 1] = current #0(1)
                print(f"Moving {current} element to {next_number} position")#0(1)
                list_of_numbers[num] = next_number #0(1)
                
        if not swapped: #0(1)
            break



my_list = [8, 14, -99, 0, 23, -4, 1]
bubble_sort(my_list)
print(my_list)
