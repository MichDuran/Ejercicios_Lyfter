# Cree una estructura de objetos que asemeje un Double Ended Queue.
# Debe incluir los métodos de push_left y push_right (para agregar nodos al inicio y al final) y 
# pop_left y pop_right (para quitar nodos al inicio y al final).
# Debe incluir un método para hacer print de toda la estructura.
# No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.

class Node:
    data = str
    next = "Node"
    prev = "Node"
    
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
        
class DoubleEndedQueue:
    
    def __init__(self):
        self.head = None
        self.tail = None

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
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_left(self):
        if self.head is None:
            raise ValueError("Double Ended Queue vacío")

        popped_data = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return popped_data

    def pop_right(self):
        if self.tail is None:
            raise ValueError("Double Ended Queue vacío")

        popped_data = self.tail.data
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        return popped_data

    def print_deque(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next
            

my_DEQ = DoubleEndedQueue()
print ("PUSH LEFT")
my_DEQ.push_left("Primer nodo (push_left)")
my_DEQ.push_left("Segundo nodo (push_left)")
my_DEQ.print_deque()

print ("PUSH RIGHT")
my_DEQ.push_right("Tercer nodo (push_right)")
my_DEQ.push_right("Cuarto nodo (push_right)")
my_DEQ.print_deque()

print ("POP LEFT")
my_DEQ.pop_left()
my_DEQ.print_deque()

print ("POP RIGHT")
my_DEQ.pop_right()
my_DEQ.print_deque()