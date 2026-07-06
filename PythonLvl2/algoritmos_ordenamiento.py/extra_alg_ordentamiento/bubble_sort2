def bubble_sort(queue):

    if queue.head is None:
        print("Queue is empty")
        return
    
    swapped = True
    while swapped:
        swapped = False
        current_node = queue.head

        while current_node.next is not None:
            if current_node.data > current_node.next.data:
                
                current_node.data, current_node.next.data = current_node.next.data, current_node.data
                swapped = True
            current_node = current_node.next
        



class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, head=None):
        self.head = head


def print_structure(queue):
    current_node = queue.head
    while current_node is not None:
        print(current_node.data, end=" → ") 
        current_node = current_node.next



class Queue(LinkedList):


    def __init__(self):
        self.tail = None
        self.head = None


    def enqueue(self, data):
        new_node = Node(data)


        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node 

        
    def dequeue(self):
        if self.head is None:
            print("Head is empty")
            return None
            
        removed_node = self.head.data

        self.head = self.head.next
        print("Removing node")
            
        return removed_node





my_queue = Queue()
my_queue.enqueue(5)
my_queue.enqueue(3)
my_queue.enqueue(8)
my_queue.enqueue(-11)
my_queue.enqueue(0)
bubble_sort(my_queue)
print_structure(my_queue)