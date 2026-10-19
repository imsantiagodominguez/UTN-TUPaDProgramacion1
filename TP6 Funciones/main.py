import package_u6.funciones as fs # fs = first steps =)

print("¡Bienvenido a mi resolución del Trabajo Práctico de la Unidad 6 - Funciones\nby: Santiago Dominguez.")

fs.separador()

print("--> Ejer. 1 - ¡Hola Mundo!")
fs.imprimir_hola_mundo() # Llamada a función Ejer. 1

fs.separador()

print("--> Ejer. 2 - Saludo a usuario.")
# Solicitud de nombre:
nombre = input("-> Ingrese su nombre: ")

fs.saludar_usuario(nombre) # Llamada a función Ejer. 2

fs.separador()

print("--> Ejer. 3 - Información de usuario.")
# Solicitud de datos:
nombre = input("-> Ingrese su nombre: ")
apellido = input("-> Ingrese su apellido: ")
edad = input("-> Ingrese su edad: ")

residencia = input("-> Ingrese su lugar de residencia: ")
fs.informacion_personal(nombre, apellido, edad, residencia) # Llamada a función Ejer. 3

fs.separador()

print("--> Ejer. 4.1 - Área de un círculo mediante radío.")
# Solicitud de radio del círculo a calcular el área.
radio = float(input("-> Ingrese el radío de su círculo: "))

salida_area = fs.calcular_area_circulo(radio) # Llamada a función Ejer. 4 y se guarda resultado en una variable.
print(f"El área del círculo es de: {salida_area}")

fs.separador()

print("--> Ejer. 4.2 - Perímetro de un círculo mediante radío.")
# Solicitud de radio del círculo a calcular el área.
radio = float(input("-> Ingrese el radío de su círculo: "))

salida_perimetro = fs.calcular_perimetro_circulo(radio) # Llamada a función Ejer. 4.2 y se guarda resultado en una variable.
print(f"El perímetro del círculo es de: {salida_perimetro}")

fs.separador()

print("--> Ejer. 5 - Segundos a horas.")
# Solicitud de segundos.
segundos = float(input("-> Ingrese la cantidad de segundos que quiere convertir en horas: "))

cantidad_horas = fs.segundos_a_horas(segundos) # Llamada a función Ejer. 5 y se guarda resultado en una variable.
print(f"La cantidad de {segundos} segundos equivale a {cantidad_horas} en horas.")#

fs.separador()#

print("--> Ejer. 6 - Tabla de multiplicación (1-10) de un número.")
# Solicitud de número.
numero = int(input("-> Ingrese el número del que desea ver su tabla de multiplicar: "))#

fs.tabla_multiplicar(numero) # Llamada de función Ejer. 6

fs.separador()#

print("--> Ejer. 7 - Operaciones básicas.")
# Solicitud de números para parámetro.
a = float(input("-> Ingrese el primero número: "))
b = float(input("-> Ingrese el segundo número: "))#

suma, resta, multiplicacion, division = fs.operaciones_basicas(a, b) # Llamada de función Ejer. 7 y se guarda los resultados en variables distintas.
print(f"\n>> Resultado suma = {suma}\n>> Resultado resta = {resta}\n>> Resultado multiplicación = {multiplicacion}\n>> Resultado división = {(division)}")
if b == 0:
    print("El programa principal informa que no se puede dividir por cero.")

fs.separador()

print("--> Ejer. 8 - Cálculo de IMC (índicie de masa corporal).")
# Solicitud de datos.
peso = float(input("-> Ingrese el peso en kilogramos: "))
altura = float(input("-> Ingrese la altura en metros: "))

total_imc = fs.calcular_imc(peso, altura) # Llamada de función Ejer. 8 y se guarda el resultado en variable.
print(f"\nEl IMC (Índice de Masa Corporal) es de: {total_imc}.")

fs.separador()

print("--> Ejer. 9 - Convertidor de temperatura en grados Celsius a Fahrenheit. ")
fs.celsius_a_fahrenheit() # Llamada de función Ejer. 9 y se imprime el resultado dentro de la misma.

fs.separador()

print("--> Ejer. 10 - Calcular el promedio de tres números ingresados.-")
fs.calcular_promedio() # Llamada de función Ejer. 10.

print("\n(!) Trabajo Práctico - Funciones --> Finalizado.\n ¡Saludos atte. Santiago!")