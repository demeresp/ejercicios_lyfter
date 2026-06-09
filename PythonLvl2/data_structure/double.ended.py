class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        self.prev = None


class LinkedList:
    def __init__(self, head):
        self.head = head
        
    
    def print_structure(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end="->")
            current_node = current_node.next



class DoubleQueue(LinkedList):

    def __init__(self):
        self.tail = None
        self.head = None


    def push_left(self, data):
        new_node = Node(data)

        if self.head is None:       
            self.head = new_node
            self.tail = new_node
        else:                           
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node        


    def push_right(self, data):
        new_node = Node(data)

        if self.tail is None:                    # Caso vacío
            self.head = new_node
            self.tail = new_node
        else:                                    # Ya hay nodos
            new_node.prev = self.tail            #  El nuevo nodo apunta hacia atrás (al viejo tail)
            self.tail.next = new_node            # El viejo tail apunta hacia adelante (al nuevo)
            self.tail = new_node# ←Actualizamos tail


    def pop_left(self):

        if self.head is None:
            print("There are no nodes to remove")
        else:
            removed_data = self.head
            self.head = self.head.prev
            return removed_data.data


    def pop_right(self):
        if self.tail is None:
            print("There are no nodes to remove")
        else:
            removed_data = self.tail
            self.tail = self.tail.prev
        return removed_data.data


miqiu = DoubleQueue()

miqiu.push_right("unpush")
miqiu.push_left("dospush") 
miqiu.push_right("trespush")

miqiu.print_structure()