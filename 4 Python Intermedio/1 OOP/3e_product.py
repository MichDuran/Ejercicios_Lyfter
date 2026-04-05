# Cree una clase Product con:
# Nombre, precio y cantidad
# Cree una clase Inventory que:
# Guarde productos en una lista
# Tenga métodos para:
# Agregar un producto
# Mostrar todos los productos
# Calcular el valor total del inventario
# Ejemplo:
# Entrada:
# product1 = Product("Mouse", 5000, 3)
# product2 = Product("Teclado", 8000, 2)
# Salida:
# print(product.calculate_total_value_of_inventory) #31000

class Product:
    def __init__(self, name, price, units):
        self.name = name
        self.price = price
        self.units = units

    def get_total_value(self):
         total_value = self.price * self.units
         return total_value
        

class Inventory:
        def __init__(self):
             self.products = []

        def add_products(self, product):
             self.products.append(product)
             print(f"Producto {product.name} agregado correctamente")
        
        def show_products(self):
             if not self.products:
                  print("No hay productos en el inventario")
                  return
             print("\nLista de productos:")
             for product in self.products:
                  print(f"Nombre: {product.name}")
                  print(f"Precio: ${product.price}")
                  print(f"Cantidad: {product.units}")
                  print(f"Valor total: ${product.get_total_value()}\n")                       
        
        def calculate_total_value_of_inventory(self):
             total = 0
             for product in self.products:
                  total += product.get_total_value()
             return total
             

def main():
     inventory = Inventory()
     product_1 = Product("Mouse", 5000, 3)
     product_2 = Product("Teclado", 8000, 2)

     inventory.add_products(product_1)
     inventory.add_products(product_2)
     inventory.show_products()

     print("Valor total del inventario:")
     print(f"${inventory.calculate_total_value_of_inventory()}")

if __name__ == "__main__":
     main()
