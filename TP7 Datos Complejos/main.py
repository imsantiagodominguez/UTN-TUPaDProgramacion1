print("¡Bienvenido a mi resolución del Trabajo Práctico de la Unidad 7 - Datos Complejos\nby: Santiago Dominguez.")

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

print()

print("--> Ejercicio 3 - Lista de frutas.")
'''Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, se debe crear una lista que contenga únicamente las
frutas, sin los precios.'''

frutas = precios_frutas.keys()

print(list(frutas))

print()

print("--> Ejercicio 4 - Agenda de contactos")
'''Se debe desarrollar un programa que permita almacenar y consultar números telefónicos.
El programa debe permitir al usuario cargar 5 contactos con su nombre como clave y número como valor.
Luego, debe pedir un nombre y mostrar el número asociado, si existe.

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