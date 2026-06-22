from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


restaurante = Restaurante("MOCCA RESTAURANT")

producto1 = Producto("Hamburguesa", 5.50, "Comida")
producto2 = Producto("Capucchino", 5.00, "Bebida")
producto3 = Producto("Lasaña", 8.00, "Comida")
producto4 = Producto("Frappe de oreo", 4.00, "Bebida")
producto5 = Producto("alitas bbq 7 alitas", 10.00, "Comida")
producto6 = Producto("Coca Cola personal", 1.00, "Bebida")

cliente1 = Cliente("Soledad Constante", "0996315153")
cliente2 = Cliente("Adriana Ulloa", "0993939395")
cliente3 = Cliente("Milena Rios", "09929399399")
cliente4 = Cliente("Camila Proaño", "0993939395")

restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)
restaurante.agregar_producto(producto3)
restaurante.agregar_producto(producto4)
restaurante.agregar_producto(producto5)
restaurante.agregar_producto(producto6)

restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)
restaurante.agregar_cliente(cliente3)
restaurante.agregar_cliente(cliente4)

print("    SISTEMA DE MOCCA   ")
print("Nombre:", restaurante.nombre)

restaurante.mostrar_productos()
restaurante.mostrar_clientes()