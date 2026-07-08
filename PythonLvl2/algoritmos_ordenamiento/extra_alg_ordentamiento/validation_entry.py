def elemnts_getter(bubble):
    def wrapper(list_of_num):
        if not list_of_num:
            print("List is empty")
            return
        
        for num in list_of_num:
            if not isinstance(num, (int,float,bool)):
                print("Element is not a number")
                return
        return bubble(list_of_num)
    return wrapper


@elemnts_getter
def bubble_sort(list_of_numbers):


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
            else:
                print(f"{current} not moved")
            

        if not swapped:
            break

    
my_list = [8, 14, -99, 0, 23, -4, 1]
bubble_sort(my_list)
