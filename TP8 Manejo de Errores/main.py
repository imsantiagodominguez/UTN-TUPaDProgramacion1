print("¡Bienvenido a mi resolución del Trabajo Práctico de la Unidad 8 - Manejo de Errores\nby: Santiago Dominguez.")#
print("v" * 50)
print()

print("--> Ejercicio 1 · Identificar los errores")
'''Identifica los errores del código usando comentarios (#) en las líneas afectadas. Indica el
tipo de error y una breve explicación de por qué ocurre.
Ejemplo: c = a / b # Error: TypeError. 'b' es un string y no permite la división.'''

a = 10
b = input("Introduce un número: ")
#result = a / b # TypeError ya que se esta queriendo realizar una división entre 'a' que es de tipo int y b que es de tipo str.
#print(f"Resultado: {result}")
numbers = [1, 2, 3]
#print(numbers[5]) # IndexError ya que se quiere imprimir por pantalla un indice que no existe en la lista numbers.
print()

print("--> Ejercicio 2 · Corregir sin excepciones")
'''Utilizando el código del ejercicio 1, arreglar los errores para que la ejecución del programa
sea correcta sin necesidad de usar excepciones.'''

a = 10
b = int(input("Introduce un número: "))
while True:
    b = int(input("Introduce un número: "))
    if b != 0:
        break
    else:
        continue
result = a / b
print(f"Resultado: {result}")

numbers = [1, 2, 3]
print(numbers[2])
print()