class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class LinkedList:
    def __init__(self, root=None):
        self.root = root
        
    def print_structure(self):
        self._print_in_order(self.root)
        print()

    def _print_in_order(self, node): #metodo recursivo
        if node is None:
            return
        

        self._print_in_order(node.left)
        print(node.data, end=" -> ")
        self._print_in_order(node.right)


class BTree(LinkedList):

    def __init__(self):
        super().__init__()          

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        current_node = self.root

        while current_node is not None:
            if data < current_node.data:
                if current_node.left is None:
                    current_node.left = new_node
                    return
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return
                current_node = current_node.right



tree = BTree()

tree.insert(10)
tree.insert(2)
tree.insert(3)
tree.insert(15)
tree.insert(8)

tree.print_structure()