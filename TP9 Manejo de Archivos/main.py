print('''¡Bienvenido a mi solución al TP9 - Manejo de Archivos!
Alumno: Santiago Dominguez''')
print("_"*70)

import os

'''Consigna 1. Crear archivo inicial con productos: Crear productos.txt con tres productos, uno por
línea: nombre,precio,cantidad. Usar campos sin comas ni saltos internos y punto
decimal en el precio.'''
print('''(>) Solución Ejer. 1:\n''')

# Se comprueba si productos.txt existe.
# Si no existe, se crea con los tres productos iniciales.
try:
    if not os.path.exists("productos.txt"):
        print(">> Se crea productos.txt")

        with open("productos.txt", "w") as archivo:
            archivo.write("Producto1,10.2,5\n")
            archivo.write("Producto2,20.9,3\n")
            archivo.write("Producto3,15.5,8\n")
    else:
        print(">> Se encontró productos.txt. Se conservan los datos existentes.")

except OSError as e:
    print(f"(ERROR!) << No se pudo inicializar el archivo: {e} >>")
    
print("_"*70)
'''Consigna 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
formato:
Producto: Lapicera | Precio: $120.5 | Cantidad: 30'''
print('''(>) Solución Ejer. 2:\n''')

# Se abre productos.txt en modo Read para leer las lineas y asi imprimir su contenido.
print('''>> Se abre productos.txt y se muestra los productos cargados en ella:''')

try:
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
except ValueError:
    print("(ERROR!) << El archivo contiene registros con un formato incorrecto >>")
except FileNotFoundError:
    print("(ERROR!) << El archivo 'productos.txt' no existe >>")
except PermissionError:
    print("(ERROR!) << No se tienen los permisos necesarios para leer el archivo >>")    
except Exception as e:
    print(f"(ERROR!) << Ha ocurrido un error inesperado: {e} >>")

print("_"*70)
'''Consigna 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
cantidad) y lo agregue al archivo sin borrar el contenido existente.'''
print('''(>) Solución Ejer. 3\n''')

#  1. Validación de cantidad a ingresar
while True:
    try:
        cantidad_nuevos = int(input(">> Ingrese la cantidad de productos que desea agregar (número entero no negativo): "))
        if cantidad_nuevos >= 0:
            break
        else:
            print("(ERROR!) << Debe ser un número mayor o igual que 0 >>")
    except ValueError:
        print("(ERROR!) << Se espera una cantidad de forma númerica y entera positiva >>")
    except Exception as e:
        print(f"(ERROR!) << Ha ocurrido un error inesperado: {e} >>")

# 2. Bucle para pedir y guardar cada producto
try:
    with open("productos.txt", "a") as archivo:
        for i in range(cantidad_nuevos):
            print("_"*70)
            print('''>> Ingrese los datos del producto nuevo a agregar:''')
            # Validación para el nombre del producto
            while True:
                nombre = input("-> Ingrese el nombre: ").strip()
                if nombre == "":
                    print("(ERROR!) << El nombre no puede estar vacío >>")
                elif "," in nombre:
                    print("(ERROR!) << El nombre no puede contener comas >>")
                else:
                    break
 
            # Validación para el precio del producto
            while True:                
                try:
                    precio = float(input("-> Ingrese el precio: "))
                    if precio > 0:
                        break
                    else:
                        print("(ERROR!) << El precio debe ser un número positivo mayor a 0 >>")
                except ValueError:
                    print("(ERROR!) << Se espera un número válido (use punto para decimales) >>")
                    
            # Validación para la cantidad del producto
            while True:
                try:
                    cantidad = int(input("-> Ingrese la cantidad: "))
                    if cantidad >= 0:
                        break
                    else:
                        print("(ERROR!) << La cantidad debe ser un número entero mayor o igual que 0 >>")
                except ValueError:
                    print("(ERROR!) << Se espera una cantidad de forma númerica y entera positiva >>")
                    
            # Se escribe en el archivo con su correspondiente salto de línea
            archivo.write(f"{nombre},{precio},{cantidad}\n")
    print(f"\n(>) Se agregaron {cantidad_nuevos} producto(s) a 'productos.txt' exitosamente.")
except PermissionError:
    print("(ERROR!) << No se tienen los permisos necesarios para modificar el archivo >>")
except OSError as e:
    print(f"(ERROR!) << Error al acceder o escribir en el archivo: {e} >>")
except Exception as e:
    print(f"(ERROR!) << Ha ocurrido un error inesperado: {e} >>")

print("_"*70)
'''Consigna 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
una lista llamada productos, donde cada elemento sea un diccionario con claves:
nombre, precio, cantidad.'''
print('''(>) Solución Ejer. 4\n''')

productos = []

try:
    lectura_correcta = False
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
    lectura_correcta = True
                
except ValueError:
    print("(ERROR!) << El archivo contiene registros con un formato incorrecto >>")
    lectura_correcta = False
except FileNotFoundError:
    print("(ERROR!) << El archivo 'productos.txt' no existe >>")
    lectura_correcta = False
except PermissionError:
    print("(ERROR!) << No se tienen los permisos necesarios para leer el archivo >>")    
    lectura_correcta = False
except Exception as e:
    print(f"(ERROR!) << Ha ocurrido un error inesperado: {e} >>")
    lectura_correcta = False

# Se muestra por pantalla la lista confeccionada finalmente.
print(productos)

print("_"*70)
'''Consigna 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
no existe, mostrar un mensaje de error.'''
print('''(>) Solución Ejer. 5\n''')

if lectura_correcta:
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
else:
    print("(ERROR!) << No se puede realizar la búsqueda porque los productos no se cargaron correctamente >>")
    
print("_"*70)
'''Consigna 6. Guardar los productos actualizados: Tras leer, buscar o agregar productos,
mantener la lista actualizada con todos los registros y sobrescribir productos.txt
desde ella, sin perder los productos incorporados.'''
print('''(>) Solución Ejer. 6\n''')

guardado_correcto = False

if lectura_correcta:
    try:
        # Se abre productos.txt en modo 'w' para sobrescribirlo
        # con el contenido actualizado de la lista productos.
        with open("productos.txt", "w") as archivo:
            for p in productos:
                archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

        guardado_correcto = True
        print("(>) El archivo 'productos.txt' se guardó correctamente.")

    except PermissionError:
        print("(ERROR!) << No se tienen los permisos necesarios para modificar el archivo >>")
    except OSError as e:
        print(f"(ERROR!) << Error al guardar el archivo: {e} >>")
    except Exception as e:
        print(f"(ERROR!) << Ha ocurrido un error inesperado: {e} >>")

else:
    print("(ERROR!) << No se puede guardar porque los productos no se cargaron correctamente >>")


# Se verifica por pantalla cómo quedó el archivo finalmente.
if guardado_correcto:
    try:
        print("\n>> Contenido final del archivo guardado:")
        with open("productos.txt", "r") as archivo:
            print(archivo.read())

    except FileNotFoundError:
        print("(ERROR!) << No se encontró el archivo para verificar su contenido >>")
    except PermissionError:
        print("(ERROR!) << No se tienen permisos para leer el archivo >>")
    except OSError as e:
        print(f"(ERROR!) << Error al leer el archivo: {e} >>")

else:
    print("\n>> No se puede verificar el guardado porque no se confirmó su ejecución.")
    
print("_"*70)
print('''<<< FIN DE TRABAJO PRACTICO Nº9 - Manejo de Archivos >>>
Muchas gracias, hasta pronto.''')