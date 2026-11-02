print('''¡Bienvenido a mi solución al TP9 - Manejo de Archivos!
Alumno: Santiago Dominguez''')
print("_"*70)

'''Consigna 1. Crear archivo inicial con productos: Crear productos.txt con tres productos, uno por
línea: nombre,precio,cantidad. Usar campos sin comas ni saltos internos y punto
decimal en el precio.'''
print('''(>) Solución Ejer. 1:\n''')
print(">> Se crea productos. txt")

with open("productos.txt", "w") as archivo:
    archivo.write("Producto1,10,5\n")
    archivo.write("Producto2,20,3\n")
    archivo.write("Producto3,15,8\n")

print("_"*70)
'''Consigna 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
formato:
Producto: Lapicera | Precio: $120.5 | Cantidad: 30'''
print('''(>) Solución Ejer. 2:\n''')

print('''>> Se abre productos.txt y se muestra los productos cargados en ella:''')
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Nombre de producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")

print("_"*70)
'''3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
cantidad) y lo agregue al archivo sin borrar el contenido existente.'''
print('''(>) Solución Ejer. 3\n''')