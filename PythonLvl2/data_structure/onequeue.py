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
  


first_queue = Queue()
first_queue.enqueue("Nodo1")
first_queue.enqueue("Nodo2")
first_queue.enqueue("Nodo3")

#print(first_queue.dequeue())
#print(first_queue.dequeue())

first_queue.print_structure() 