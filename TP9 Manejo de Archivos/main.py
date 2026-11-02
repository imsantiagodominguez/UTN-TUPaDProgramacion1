print('''¡Bienvenido a mi solución al TP9 - Manejo de Archivos!
Alumno: Santiago Dominguez''')
print("_"*70)

'''Consigna 1. Crear archivo inicial con productos: Crear productos.txt con tres productos, uno por
línea: nombre,precio,cantidad. Usar campos sin comas ni saltos internos y punto
decimal en el precio.'''
print('''(>) Solución Ejer. 1:\n''')
print(">> Se crea productos. txt")
# Se abre productos.txt en modo Write, para en caso de que no exista lo cree, si existe lo sobreescribirá para una ejecución esperada.
with open("productos.txt", "w") as archivo:
    archivo.write("Producto1,10.2,5\n")
    archivo.write("Producto2,20.9,3\n")
    archivo.write("Producto3,15.5,8\n")

print("_"*70)
'''Consigna 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
formato:
Producto: Lapicera | Precio: $120.5 | Cantidad: 30'''
print('''(>) Solución Ejer. 2:\n''')
# Se abre productos.txt en modo Read para leer las lineas y asi imprimir su contenido.
print('''>> Se abre productos.txt y se muestra los productos cargados en ella:''')
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Nombre de producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")

print("_"*70)
'''Consigna 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
cantidad) y lo agregue al archivo sin borrar el contenido existente.'''
print('''(>) Solución Ejer. 3\n''')
print('''>> Ingrese los datos del producto nuevo a agregar:''')
# Solicitud de datos para el producto a agregar
nombre = input("-> Ingrese el nombre: ")
precio = input("-> Ingrese el precio: ")
cantidad = input("-> Ingrese la cantidad: ")

try:
    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
# Se agrega except para caso donde el archivo no se encuentre.
except FileNotFoundError:
    print("(ERROR!) << El archivo productos.txt no existe >>")
# Se agrega except para cualquier otro caso inesperado.
except Exception as e:
    print(f"(ERROR!) << Ha ocurrido un error inesperado: {e} >>")
# Se utiliza finally para enseñar por pantalla que el producto ingresado por el usuario fue añadido al .txt
finally:
    print("(>) Producto añadido a 'productos.txt' exitosamente.")

print("_"*70)
'''Consigna 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
una lista llamada productos, donde cada elemento sea un diccionario con claves:
nombre, precio, cantidad.'''
print('''(>) Solución Ejer. 4\n''')

productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        # Se limpia el salto de línea y se separan los campos por coma
        nombre, precio, cantidad = linea.strip().split(",")
        # Se crea el diccionario solicitado:
        producto = {"nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                    }
        productos.append(producto)
# Se muestra por pantalla la lista confeccionada finalmente.
print(productos)

print("_"*70)
'''Consigna 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
no existe, mostrar un mensaje de error.'''
print('''(>) Solución Ejer. 5\n''')

buscar_producto = input(">> Ingrese el producto a buscar en la lista: ").strip()
# Se utiliza una variable booleana para registrar si se halló el producto
encontrado = False

for p in productos:
    # Se utiliza .lower() en la comparación porque permite que encuentre el producto sin importar si se escribió en mayúsculas o minúsculas.
    if p["nombre"].lower() == buscar_producto.lower():
        print(''' >> Producto encontrado. Sus datos son los siguientes:''')
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")        
        encontrado = True
        break
# Caso de no existir el producto ingresado
if not encontrado:
    print("(ERROR!) << El producto ingresado no se ha encontrado >>")

print("_"*70)
'''Consigna 6. Guardar los productos actualizados: Tras leer, buscar o agregar productos,
mantener la lista actualizada con todos los registros y sobrescribir productos.txt
desde ella, sin perder los productos incorporados.'''
print('''(>) Solución Ejer. 6\n''')

# Se abre productos.txt en modo 'w' para sobreescribirlo con el contenido actual de la lista 'productos'
with open("productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("(>) El archivo 'productos.txt' ha sido actualizado y guardado correctamente.")

# Se verifica por pantalla cómo quedó el archivo finalmente
print("\n>> Contenido final del archivo guardado:")
with open("productos.txt", "r") as archivo:
    print(archivo.read())
    
print("_"*70)
print('''<<< FIN DE TRABAJO PRACTICO Nº9 - Manejo de Archivos >>>
Muchas gracias, hasta pronto.''')