# Cree una estructura de objetos que asemeje un Stack.
# Debe incluir los métodos de push (para agregar nodos) y pop (para quitar nodos).
# Debe incluir un método para hacer print de toda la estructura.
# No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.

class Node:
    data = str
    next = "Node"
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise ValueError("Stack vacío")

        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def print_stack(self):
        current = self.top

        while current is not None:
            print(current.data)
            current = current.next


my_stack = Stack()
print ("PUSH")
my_stack.push("Primer nodo")
my_stack.push("Segundo nodo")
my_stack.push("Tercer nodo")
my_stack.push("Cuarto nodo")

my_stack.print_stack()

print ("POP")
my_stack.pop()
my_stack.print_stack()

print ("POP")
my_stack.pop()
my_stack.print_stack()

print ("POP")
my_stack.pop()
my_stack.print_stack()

print ("POP")
my_stack.pop()
my_stack.print_stack()

print ("POP (debe estar vacío)")
my_stack.pop()
my_stack.print_stack()