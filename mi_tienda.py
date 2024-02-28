class Producto:
    def __init__(self, nombre, precio,cantidad_en_stock):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_en_stock = cantidad_en_stock
    
class CarritoDeCompras:
    
    def __init__(self):
        self.productos = []
        
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total
    
# Creamos algunos Productos
producto1= Producto("Camiseta", 18000,0)
producto2= Producto("Medias", 9000,0)
producto3= Producto("Pantalon Corto", 12000,0)

# Creamos un carrito de compras y agregamos productos
carrito = CarritoDeCompras()
carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)
carrito.agregar_producto(producto3)

#Calculamos el total de la compra
total_compra = carrito.calcular_total()
print(f'Total de la compra: ${total_compra: .2f}')

        
        