# Unidad 9: Manejo de archivos
# Alumno: Santiago Dominguez

'''Consigna 1. Crear archivo inicial con productos: Crear productos.txt con tres productos, uno por
línea: nombre,precio,cantidad. Usar campos sin comas ni saltos internos y punto
decimal en el precio.'''

with open("productos.txt", "w") as archivo:
    archivo.write("Producto1,10,5\n")
    archivo.write("Producto2,20,3\n")
    archivo.write("Producto3,15,8\n")