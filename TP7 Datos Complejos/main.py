from collections import Counter

print("¡Bienvenido a mi resolución del Trabajo Práctico de la Unidad 7 - Datos Complejos\nby: Santiago Dominguez.")#
print("--> Ejercicio 1 - Diccionario de precios.")
'''Dado el diccionario precios_frutas :'''
precios_frutas = {
    "Banana": 1200,
    "Ananá": 2500,
    "Melón": 3000,
    "Uva": 1450,
}
'''Se deben añadir las siguientes frutas con sus respectivos precios:
Naranja = 1200
Manzana = 1500
Pera = 2300'''
print(precios_frutas)
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)
print('''>>> FIN EJERCICIO 1 <<< ''')
print()

print("--> Ejercicio 2 - Actualizar precios.")
'''Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, se deben actualizar los precios de las siguientes frutas:
Banana = 1330
Manzana = 1700
Melón = 2800'''
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800
print(precios_frutas)
print('''>>> FIN EJERCICIO 2 <<< ''')
print()

print("--> Ejercicio 3 - Lista de frutas.")
'''Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, se debe crear una lista que contenga únicamente las
frutas, sin los precios.'''#
frutas = precios_frutas.keys()
print(list(frutas))
print('''>>> FIN EJERCICIO 3 <<< ''')
print()

print("--> Ejercicio 4 - Agenda de contactos.")
'''Se debe desarrollar un programa que permita almacenar y consultar números telefónicos.
-El programa debe permitir al usuario cargar 5 contactos con su nombre como clave y número como valor.
-Luego, debe pedir un nombre y mostrar el número asociado, si existe.#
Ejemplo:
contactos = {"Juan": "123456", "Ana": "987654"}
Consultar: "Juan" -> muestra "123456"
'''
agenda = {}
cantidad_contactos = 3
for cantidad_contactos in range (3):
    nombre = input(f"-> Ingrese el NOMBRE del contacto Nº{cantidad_contactos+1} a añadir a la Agenda de Contactos: ")
    telefono = input(f"-> Ingrese el teléfono del mismo: ")
    agenda[nombre] = telefono
    print()
consulta = input("-> Ingrese el NOMBRE del contacto a consultar: ")
if not consulta in agenda:
    print("(!) El NOMBRE del contacto ingresado no existe en la agenda de contactos.")
else:
    print(agenda[consulta])
print('''>>> FIN EJERCICIO 4 <<< ''')
print()

print("--> Ejercicio 5 - Palabras únicas y conteo.")
'''El programa debe solicitar al usuario una frase e imprimir:
-Las palabras únicas (usando un set).
-Un diccionario con la cantidad de veces que aparece cada palabra.
Ejemplo:
Entrada -> "hola mundo hola"
Salida:
Palabras_únicas: {'hola', 'mundo'}
Recuento: {'hola': 2, 'mundo': 1}'''
frase = input("-> Ingrese una frase: ") 
cant_palabras_unicas = frase.split()
print(len(set(cant_palabras_unicas)))
cant_x_palabra = Counter(cant_palabras_unicas)
print(dict(cant_x_palabra))
print('''>>> FIN EJERCICIO 5 <<< ''')
print()

print("--> Ejercicio 6 - Promedio de notas por alumno.")
'''El programa debe permitir ingresar los nombres de 3 alumnos y, para cada uno, una tupla
de 3 notas. Luego, debe mostrar el promedio de cada alumno.
Ejemplo:
alumnos = {
"Sofía": (10, 9, 8),
"Luis": (6, 7, 7),
"Marta": (8, 9, 9)
}'''
alumnos = {}
cantidad_alumnos = 3
for cantidad_alumnos in range(3):
    # Solicitud de datos
    nombre = input(f"-> Ingrese el NOMBRE del Alumno Nº {cantidad_alumnos+1}: ")
    nota1 = int(input("-> Ingrese la 1er nota: "))
    nota2 = int(input("-> Ingrese la 2da nota: "))
    nota3 = int(input("-> Ingrese la 3er nota: "))
    notas = (nota1, nota2, nota3)
    alumnos[nombre] = notas # Se añade la clave nueva (alumno en este caso) y se le asigna como valor la tupla con las tres notas del alumno.
# Calcúlo de promedios:
for nombre, notas in alumnos.items():
    promedio = round(sum(notas)/3, 2)
    print(f"El promedio de {nombre} es: {promedio}")#
print('''>>> FIN EJERCICIO 6 <<< ''')
print()

print("--> Ejercicio 7 - Asistencia a una capacitación.")
'''Se recibe el registro diario de asistencia a una capacitación en forma de lista. En dicha lista
pueden aparecer nombres repetidos, ya que una misma persona pudo haber asistido en
más de una jornada.

Ejemplo:
asistencias = ["Ana", "Luis", "Ana", "María", "Luis", "Pedro", "Ana"]

El programa debe:
-Mostrar la lista original de asistencias.
-Generar un conjunto (set) a partir de la lista y mostrar las personas que asistieron al menos una vez (sin repetir nombres).
-Indicar cuántas veces asistió cada persona a la capacitación'''

asistencias = []
cant_asistencias = int(input("-> Ingrese la cantidad de asistencias, en número entero, a registrar: "))

for i in range(cant_asistencias):
    asist = input("-> Ingrese el nombre de la persona que asistió: ")
    asistencias.append(asist)

print()
# Se imprime la lista original de asistencias.
print(f">> La lista de asistencias es: {sorted(asistencias)}") # Se muestra la lista original ingresada y ordenada alfabeticamente.

print()
# Se genera un conjunto a partir de la lista y muestra las personas que asistieron al menos una vez, sin repetir nombres.
quien_asist = set(asistencias)
for i in sorted(quien_asist):
    print(f">> {i} ha asistido al menos una vez.") # Imprime nombre por nombre.

print()
# Se indica cuantas veces asistió cada persona a la capacitación.
for i in sorted(quien_asist):
    cant_asistio = asistencias.count(i)
    print(f">> {i} asistió {cant_asistio} veces.")
print('''>>> FIN EJERCICIO 7 <<< ''')
print()

print("--> Ejercicio 8 - Stock de productos.")
'''Se debe armar un diccionario donde las claves sean nombres de productos y los valores
su stock. El programa debe permitir al usuario:
-Consultar el stock de un producto ingresado.
-Agregar unidades al stock si el producto ya existe.
-Agregar un nuevo producto si no existe.'''

# Se solicita cantidad de productos a cargar:
cant_productos = int(input("-> Ingrese la cantidad de productos a cargar en el stock: "))
print()

# Se crea el diccionario y se completa con los datos que ingrese el usuario.
stock = {}
for i in range(cant_productos):
    producto = input(f'''-> Ingrese el nombre del producto nº {i+1}: ''')
    unidades = int(input(f'''-> Ingrese las unidades del producto nº {i+1}: '''))
    stock[producto] = unidades
print()

# Consulta de stock de un producto:
consulta = input('''(>) Consulta de stock de un producto.
-> Ingrese el nombre de un producto a chequear el stock: ''')
if consulta in stock:
    unidades_d_consulta = stock[consulta]
    print(f">> El stock actualizado del producto {consulta} es de {unidades_d_consulta} unidades.")
else:
    print('''***** El producto a consultar no existe *****''')
print()

# Agregar unidades al stock de un producto existente:
agregar_a_producto = input('''(>) Agregar stock de un producto existente.
(!) Si no existe el programa sigue.
-> Ingrese el nombre del producto a ingresar mas unidades al stock: ''')
if agregar_a_producto in stock:
    mas_u = int(input('''¡OK! El producto esta en el stock.
-> Ingrese las unidades a sumar al stock: '''))
    stock_actual = stock[agregar_a_producto]
    stock_actualizado = stock_actual+ mas_u
    stock[agregar_a_producto] = stock_actualizado
    print(f'''>> Se actualizo el stock del producto {producto} y ahora tiene {stock_actualizado} unidades.''')
else:
    print('''***** El producto no existe en el stock *****''')
print()

# Agregar producto si no existe:
agregar_p = input('''(>) Agregar nuevo producto.
(!) Si existe no se añáde.
-> Ingrese el nombre del producto nuevo a ingresar al stock: ''')
if agregar_p not in stock:
    unidades = int(input('''¡OK! El producto no se encuentra en el stock.
-> Ingrese las unidades del producto nuevo: '''))
    stock[agregar_p] = unidades
    # Se imprime stock con el producto añadido:
    print(f'''\n>> El stock es:''')
    for producto, unidades in stock.items():
        print(f'''* PRODUCTO: {producto} | UNIDADES: {unidades}''')
else:
    print("***** El producto ya en el stock. *****")
print('''>>> FIN EJERCICIO 8 <<<''')
print()

print('''--> Ejercicio 9 - Agenda por día y hora.''')
'''Se debe crear una agenda donde las claves sean tuplas de (día, hora) y los valores sean
eventos.
Ejemplo:
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}
El programa debe permitir consultar qué actividad hay en cierto día y hora.'''
print()

agenda = {}

cant_fechas_agendar = int(input('''-> Ingrese la cantidad de eventos a agendar: '''))
for i in range(cant_fechas_agendar):
    dia = input("-> Ingrese el día del evento a agendar: ")
    hora = input(f"-> Ingrese la hora del evento {dia} a agendar: ")
    fecha = (dia, hora)
    evento = input("-> Ingrese la actividad del evento a agandar: ")
    agenda[fecha] = evento
print()

print("(>) Consulta de actividad (dia, hora).")
consulta_dia = input("-> Ingrese el día del evento que desea consultar: ")
consulta_hora = input(f"-> Ingrese la hora del {consulta_dia} para consultar el evento agendado: ")
if (consulta_dia, consulta_hora) not in agenda:
    print(f'''***** ¡NO hay ningún evento agendado para el día: {consulta_dia} a la hora: {consulta_hora} *****''')
else:
    actividad_consulta = agenda.get((consulta_dia, consulta_hora))
    print(f'''>> La actividad agendada para el día {consulta_dia} a la hora {consulta_hora} es "{actividad_consulta}".''')
print()

print('''>>> FIN EJERCICIO 9 <<<''')
print()

print('''--> Ejercicio 10 - Invertir un diccionario.''')
'''Dado un diccionario que mapea nombres de países con sus capitales, se debe construir un
nuevo diccionario donde:
- Las capitales sean las claves.
- Los países sean los valores.
Ejemplo:
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {"Buenos Aires": "Argentina", "Santiago": "Chile"}'''

cant_paises = int(input('''-> ¿Cuantos países desea mapear?\n'''))
globo = {}

for i in range(cant_paises):
    pais = input('''-> Ingrese el país: ''').title()
    capital = input('''-> Ingrese la capital del mismo: ''').title()
    globo[pais] = capital
# Se imprime diccionario original:
print(f'''\n>> El diccionario original es:''')
print(globo)

# Invertir diccionario:
for cant_paises in globo:
    globo_invertido = {capital: pais for pais, capital in globo.items()}
# Se imprime diccionario invertido
print(f'''\n>> El diccionario original invertido es:''')
print(globo_invertido)

print()
print('''>>> FIN EJERCICIO 10 <<<''')
print()
print("(!) Trabajo Práctico - Datos Complejos --> Finalizado.\n¡Saludos atte. Santiago!")