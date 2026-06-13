class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class LinkedList:
    def __init__(self, root):
        self.root = root

    
    def print_structure(self, node):
        if node is None:
            return
        
        self.print_structure(node.left)
        print(node.data, end=" -> ")
        self.print_structure(node.right)


class BTree:

    def insert(self, data):

        new_node = Node(data)

        if new_node.left is None:
            new_node = new_node.left