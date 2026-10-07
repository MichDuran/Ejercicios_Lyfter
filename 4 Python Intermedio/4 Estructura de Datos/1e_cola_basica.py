# Cree una estructura que represente una cola básica (Queue) con objetos enlazados
# Restricción: no usar list, dict, tuple, collections
# Métodos requeridos: 
# dequeue(): elimina y retorna el nodo del inicio
# enqueue(data): agrega un nodo al final
# print_all(): imprime todos los elementos de la cola en orden

class Node:
    data = str
    next = "Node"
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
        
class Queue:
    
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            raise ValueError("Queue vacío")

        dequeued_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_data

    def print_all(self):
        current = self.front
        while current is not None:
            print(current.data, end="")
            if current.next is not None:
                print(" -> ", end="")
            current = current.next
        print()
        
        
my_queue = Queue()
print("ENQUEUE")
my_queue.enqueue("A")
my_queue.enqueue("B")
my_queue.enqueue("C")
my_queue.print_all()

print("DEQUEUE")
print(my_queue.dequeue())
my_queue.print_all()