# Resolución de Trabajo Práctico 5 - Listas x Santiago Dominguez


# Ejercicio 1
# Crear una lista con las notas de 10 estudiantes.
#   - Mostrar la lista completa
#   - Calcular y mostrar el promedio.
#   - Indicar la nota mas alta y la mas baja.

suma_notas = 0.0
promedio = 0.0
lista_notas = []
nota_min = 10.0
nota_max = 0.0

print("¡Bienvenido!\nA continuación ingrese las notas entre 0.0 y 10.0.\n")
for i in range(1,11):
    while True: # Ciclo para la solicitud y validación de notas.
        nota = input(f"Ingrese la nota Nº {i}: ").replace(',', '.')
        if not nota.isdigit() or float(nota) < 0 or float(nota) > 10:
            print("Ingrese una nota valida, entre 0.0 y 10.0.")
            continue
        else:
            nota_valida = float(nota)
            break
    if nota_valida < nota_min: # Se verifica que la nota no sea más baja que la anterior ingresada.
        nota_min = nota_valida
    if nota_valida > nota_max: # Se verifica que la nota no sea más alta que la anterior ingresada.
        nota_max = nota_valida
    suma_notas += nota_valida # Variable donde se acumula las notas ingresadas para luego calcular promedio
    lista_notas.append(nota_valida)

print() # por visual
for i in range (len(lista_notas)): # Se muestra la lista completa de notas
    print(f''' - NOTA "{i+1}": {lista_notas[i]}''')
print() # por visual
print(f" - El promedio de tus notas es de: {suma_notas/10}") # Se imprime el promedio y se cálcula en la misma línea.
print(f" - La nota más alta ingresada es: {nota_max}")
print(f" - La nota más baja ingresada es: {nota_min}")
print() # por visual


# Ejercicio 2
# Pedir al usuario que cargue 5 productos en una lista.
#   - Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#   - Preguntar al usuario qué producto desea eliminar y actualizar la lista.

lista_productos = []

for i in range (5): # Se solicitan los 5 productos.
    producto = input(f"Ingrese el producto nº {i+1}: ")
    lista_productos.append(producto)

lista_ordenada = sorted(lista_productos) # Se ordena la lista de elementos ingresada

print(f"\n - La lista de productos que ingreso es la siguiente:")
for i in range(len(lista_ordenada)): # Se imprime la lista ingresada ya ordenada
            print(f'''"{i+1}" {lista_ordenada[i]}''')

eliminar = input(" - ¿Desea eliminar un producto y actualizar la lista? (y/n): ").lower()
while True:
    if eliminar != "y" and eliminar != "n":
        print("Opción NO VÁLIDA...")
        eliminar = input(" - ¿Desea eliminar un producto y actualizar la lista? (y/n): ").lower()
        continue
    else:
        break

if eliminar == "y":
    print(f''' - ¿Qué producto desea eliminar de la lista? (1-5)
{lista_ordenada}
Siendo: 
 "1" {lista_ordenada[0]}
 "2" {lista_ordenada[1]}
 "3" {lista_ordenada[2]}
 "4" {lista_ordenada[3]}
 "5" {lista_ordenada[4]}''')
    quiero = input(" >> ")
    while True:
        if not quiero.isdigit() or int(quiero) < 1 or int(quiero) > 5:
            print("Opción NO VÁLIDA...")
            quiero = input(f''' - ¿Qué producto desea eliminar de la lista? (1-5):
 >> ''')
            continue
        else:
            break
    if quiero == "1":
        eliminado = lista_ordenada.pop(0) # Se actualiza el primer elemento por el ingresado.
        print(f" - La lista de productos actualizada es la siguiente:") # Se imprimer por pantalla la nueva lista.
        for i in range(len(lista_ordenada)):
            print(f'''PRODUCTO "{i+1}": {lista_ordenada[i]}''')
    elif quiero == "2":
        eliminado = lista_ordenada.pop(1) # Se actualiza el primer elemento por el ingresado.
        print(f" - La lista de productos actualizada es la siguiente:") # Se imprimer por pantalla la nueva lista.
        for i in range(len(lista_ordenada)):
            print(f'''PRODUCTO "{i+1}": {lista_ordenada[i]}''')
    elif quiero == "3":
        eliminado = lista_ordenada.pop(2) # Se actualiza el primer elemento por el ingresado.
        print(f" - La lista de productos actualizada es la siguiente:") # Se imprimer por pantalla la nueva lista.
        for i in range(len(lista_ordenada)):
            print(f'''PRODUCTO "{i+1}": {lista_ordenada[i]}''')
    elif quiero == "4":
        eliminado = lista_ordenada.pop(3) # Se actualiza el primer elemento por el ingresado.
        print(f" - La lista de productos actualizada es la siguiente:") # Se imprimer por pantalla la nueva lista.
        for i in range(len(lista_ordenada)):
            print(f'''PRODUCTO "{i+1}": {lista_ordenada[i]}''')
    elif quiero == "5":
        eliminado = lista_ordenada.pop(4) # Se actualiza el primer elemento por el ingresado.
        print(f" - La lista de productos actualizada es la siguiente:") # Se imprimer por pantalla la nueva lista.
        for i in range(len(lista_ordenada)):
            print(f'''PRODUCTO "{i+1}": {lista_ordenada[i]}''')
    print(f" - PRODUCTO ELIMINADO: {eliminado}.")
else:
    print("\n > NO ELIMINAR.\n - Okey, hasta pronto.")


#Ejercicio 3
# Generar una lista con 15 números enteros al azar entre 1 y 100.
#   - Crear una lista con los pares y otra con los impares.
#   - Mostrar cuántos números tiene cada lista.

import random

numeros_random = [random.randint(1, 100) for _ in range(15)] # Se genera la lista de 15 números enteros random entre 1 y 100.
lista_pares = []
lista_impares = []

for i in numeros_random: # Ciclo para recorrer la lista generada y contabilizar los pares e impares.
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)

# Se imprime la lista original de números random
print(f''' - La lista original es:''')
for i in range(15): 
    print(f'''Número {i+1} = {numeros_random[i]}''')
# Se imprime la lista de pares
print(f'''\n - La lista de pares es:''')
for i in range(len(lista_pares)):
    print(f'''Número {i+1} = {numeros_random[i]}''')
# Se imprime la lista de impares
print(f'''\n - La lista de impares es:''')
for i in range(len(lista_impares)):
    print(f'''Número {i+1} = {numeros_random[i]}''')
# Ejercicio 4
# Dada una lista con valores repetidos:
#   - Crear una nueva lista sin elementos repetidos.
#   - Mostrar el resultado.

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
print(" >> RESULTADO DE LISTA ORIGINAL. ")
for i in range(len(datos)):
    print(f'''Valor nº {i+1}: {datos[i]}''')

sin_repetir = [] # Guardamos elementos para luego 

# Se recorre la lista original y añaden al final de la vacía aquellos que no esten en ella 
for i in (datos):
    if i not in sin_repetir:
        sin_repetir.append(i)

print(" >> RESULTADO DE LISTA SIN ELEMENTOS REPETIDOS. ")
for i in range(len(sin_repetir)):
    print(f'''Valor nº {i+1}: {sin_repetir[i]}''')


# Ejercicio 5
# Crear una lista con los nombres de 8 estudiantes presentes en clase.
#   - Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#   - Mostrar la lista final actualizada.

lista_estudiantes_en_clase = []

for i in range(5):
        while True: # Validación de la entrada, para que sea de tipo caracteres
            estudiante = input(f"> Ingrese el nombre del {i+1} estudiante: ")
            if not estudiante.isalpha() or estudiante == "":
               print("(!) Nombre no válido.")
               continue
            else:
                lista_estudiantes_en_clase.append(estudiante)
                break

print('''> Pregunta:
¿Quiere agregar un nuevo estudiante o eliminar uno existente?
- Ingresar "1" para agregar un nuevo estudiante o "2" para eliminar uno existente.''')
while True:
    accion = input("> ")
    if not accion.isdigit() or int(accion) != 1 and int(accion) != 2: # Validación de acción
        print("(!) Opción no válida.")
        print('''- Ingresar "1" para agregar un nuevo estudiante o "2" para eliminar uno existente.''')
        continue
    else:
         accion_validada = int(accion)
         break
    
if accion_validada == 1: # Caso donde el usuario quiera agregar un nuevo estudiante al final de la lista ingresada
    while True: # Validación de la entrada, para que sea de tipo caracteres
        estudiante = input(f"> Ingrese el nombre del estudiante que desea agregar: ")
        if not estudiante.isalpha() or estudiante == "":
           print("(!) Nombre no válido.")
           continue
        else: 
            lista_estudiantes_en_clase.append(estudiante)
            for i in range(len(lista_estudiantes_en_clase)): # Se imprime por pantalla la lista ingresada dentro de una estructura repetitiva 
                print(f"{lista_estudiantes_en_clase[i]}")
            break
if accion_validada == 2: # Caso donde el usuario quiera eliminar un estudiante existente en la lista.
    while True:
        estudiante_eliminar = input("-> Ingrese el estudiante existente en la lista que quiera eliminar: ") # Solicitud de estudiante a eliminar.
        for i in range(len(lista_estudiantes_en_clase)): # Se recorre la lista la cantidad de veces según los elementos que contenga
            if estudiante_eliminar in lista_estudiantes_en_clase: # Si el estudiante ingresado a eliminar esta se borra de ella.
                lista_estudiantes_en_clase.remove(estudiante_eliminar) # Mediante function .remove()
                print(f'''> Se ha eliminado el estudiante "{estudiante_eliminar}" de la lista.
>La lista actualizada es:''')
                for i in range(len(lista_estudiantes_en_clase)): # Se imprime por pantalla mensaje de que ha sido eliminado y se enseña la lista actualizada.
                    print(f"{lista_estudiantes_en_clase[i]}")
                break
            else:
                print(f'''> El estudiante ingresado no esta en la lista.''') # Caso donde el estudiante a eliminar ingresado por el usuario no se ha encontrado.
                break