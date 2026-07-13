def bubble_sort_inverted(list_of_numbers):

    #vuelva por cada numero que hay en la lista\
    for i in range(len(list_of_numbers) -1, -1, -1):
        swapped = False #para verificar una condicion mas adelante.
        for num in range(len(list_of_numbers) -1, 0, -1): #el del medio donde es donde se detendra antes que llegar! o sea parara en i1
            current = list_of_numbers[num]
            next_number = list_of_numbers[num - 1]

            print(f"Num:{num}, current number:{current}, number to compare:{next_number}")
            
            if current < next_number:
                swapped = True           
                list_of_numbers[num - 1] = current
                print(f"Moving {current} element to {next_number} position")
                list_of_numbers[num] = next_number
                
        if not swapped:
            break



my_list = [10, -3, 45, 33, 2, 0, -31]
bubble_sort_inverted(my_list)
print(my_list)
