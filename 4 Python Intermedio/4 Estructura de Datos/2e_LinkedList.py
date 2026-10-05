# Cree una clase LinkedList con los métodos:
# insert_front(data): Inserta al inicio
# insert_back(data): Inserta al final
# delete(data): Elimina el primer nodo con el valor dado
# print_all(): Imprime todos los valores

class Node:
    data = str
    next = "Node"
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
        
class LinkedList:
    
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def delete(self, data):
        if self.head is None:
            raise ValueError("LinkedList vacío")

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
            raise ValueError(f"Valor {data} no encontrado en la LinkedList")

    def print_all(self):
        current = self.head
        while current is not None:
            print(current.data, end="")
            if current.next is not None:
                print(" -> ", end="")
            current = current.next
        print()
        
        
my_ll = LinkedList()
print("INSERT FRONT")
my_ll.insert_front(10)
my_ll.insert_front(20)
my_ll.print_all()

print("INSERT BACK")
my_ll.insert_back(30)
my_ll.print_all()

print("DELETE 1")
my_ll.delete(10)
my_ll.print_all()

print("DELETE 2")
my_ll.delete(40)