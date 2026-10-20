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