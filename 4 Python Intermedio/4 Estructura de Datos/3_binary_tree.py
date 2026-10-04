# Cree una estructura de objetos que asemeje un Binary Tree.
# Debe incluir un método para hacer print de toda la estructura.
# No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.


class Node:
    data = str
    left = "Node"
    right = "Node"

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
        
class BinaryTree:
    
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current_node, new_node):
        if new_node.data < current_node.data:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert_recursive(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert_recursive(current_node.right, new_node)

    def print_tree(self):
        self._print_recursive(self.root)

    def _print_recursive(self, node):
        if node is not None:
            self._print_recursive(node.left)
            print(node.data)
            self._print_recursive(node.right)
            
            
my_tree = BinaryTree()
print("INSERT")
my_tree.insert(10)
my_tree.insert(5)
my_tree.insert(20)
my_tree.insert(3)
my_tree.insert(7)
my_tree.insert(15)
my_tree.insert(30)

my_tree.print_tree()