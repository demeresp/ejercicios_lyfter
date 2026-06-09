class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:
  
  def __init__(self, head=None):
    self.head = head


  def print_structure(self):
    current_node = self.head
    while current_node is not None:
      print(current_node.data, end=" → ") 
      current_node = current_node.next


class Stack(LinkedList):
    def __init__(self, head=None):
        self.head = head


    def push(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node


    def pop(self):     
        if not self.head:
            print("There is not node to delete")
            return None
        
        else:
            removed_data = self.head.data
            self.head = self.head.next
            return removed_data
        


push1 = Stack()

push1.push("first")
push1.push("second")
push1.push("third")

push1.print_structure()