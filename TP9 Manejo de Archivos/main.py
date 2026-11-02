# Unidad 9: Manejo de archivos
# Alumno: Santiago Dominguez

'''Consigna 1. Crear archivo inicial con productos: Crear productos.txt con tres productos, uno por
línea: nombre,precio,cantidad. Usar campos sin comas ni saltos internos y punto
decimal en el precio.'''

with open("productos.txt", "w") as archivo:
    archivo.write("Producto1,10,5\n")
    archivo.write("Producto2,20,3\n")
    archivo.write("Producto3,15,8\n")

'''Consigna 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
formato:
Producto: Lapicera | Precio: $120.5 | Cantidad: 30'''

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Nombre de producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")