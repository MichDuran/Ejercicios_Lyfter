# Lista doblemente enlazada
# Requisitos: Cada nodo debe tener referencia al siguiente y al anterior.
# Métodos: 
# append(data): Agrega al final
# prepend(data): Agrega al inicio
# delete(data): Elimina el primer nodo con ese valor
# print_forward() y print_backward(): Imprime en ambas direcciones

class Node:
    data = str
    next = "Node"
    prev = "Node"
    
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
        
class DLL:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        if self.head is None:
            raise ValueError("Double LinkedList vacía")

        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                return
            current = current.next

    def print_forward(self):
        current = self.head
        while current is not None:
            print(current.data, end="")
            if current.next is not None:
                print(" -> ", end="")
            current = current.next
        print()

    def print_backward(self):
        current = self.tail
        while current is not None:
            print(current.data, end="")
            if current.prev is not None:
                print(" -> ", end="")
            current = current.prev
        print()
        
        
my_dll = DLL()
print("FORWARD APPEND")
my_dll.append("A")
my_dll.append("B")
my_dll.append("C")
my_dll.print_forward()

print("BACKWARD APPEND")
my_dll.print_backward()

print("FORWARD PREPEND")
my_dll.prepend("X")
my_dll.print_forward()

print("BACKWARD PREPEND")
my_dll.print_backward()

print("FORWARD DELETE")
my_dll.delete("B")
my_dll.print_forward()

print("BACKWARD DELETE")
my_dll.print_backward()