import math

def separador():
    print()

def imprimir_hola_mundo():
    '''Ejercicio 1: Función que imprime el mensaje "Hola Mundo!" por pantalla.'''
    print("Hola Mundo!")

def saludar_usuario(nombre):
    '''Ejercicio 2: Función que recibe como parámetro un nombre y devuelve un saludo personalizado. Por empleo:\n Ingresa "Pepé", imprime: "¡Hola Pepé!"'''
    print(f"¡Hola {nombre}!")

def informacion_personal(nombre, apellido, edad, residencia):
    '''Ejercicio 3: Función que recibe 4 parámetros: nombre, apellido, edad y residencia, y muestra por pantalla los datos del usuario de forma ordenada.'''
    print(f"Soy {nombre.title()} {apellido.title()}, tengo {edad} años y vivo en {residencia.title()}")

def calcular_area_circulo(radio):
    '''Ejercicio 4.1: Función que recibe como parámetro el radio del círculo y devuelve su área.'''
    area_circulo = round( math.pi * radio**2, 2) # Formula de cálculo del área conociendo su radio. Se utilizo pi de la lib de math y round para redondear a 2 decimales el resultado.
    return area_circulo

def calcular_perimetro_circulo(radio):
    '''Ejercicio 4.2: Función que recibe como parámetro el radio del círculo y devuelve su perímetro.'''
    perimetro_circulo = round(2 * math.pi * radio, 2) # Formula de cálculo del perímetro conociendo su radio.
    return perimetro_circulo

def segundos_a_horas(segundos):
    '''Ejercicio 5: Función que recibe como parámetro cantidad de segundos y devuelve el equivalente en horas.'''
    horas = round(segundos / 3600, 2)
    return horas

def tabla_multiplicar(numero):
    '''Ejercicio 6: Función que recibe como parámetro un número entero y devuelve su tabla de multiplicar del 1 al 10.'''
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero*i}")

def operaciones_basicas(a, b):
    '''Ejercicio 7: Función que recibe dos números como parámetros y devuelve una tupla con el resultado de
sumarlos, restarlos, multiplicarlos y dividirlos. Muestra los resultados de fomra clara. Si el segundo número es 0, la función
devuelve None en la posición de la división y el programa informa que no se puede dividir por cero.'''
    suma = (a + b)
    resta = (a - b)
    multiplicacion = (a * b)
    if b == 0:
        return float(suma), float(resta), float(multiplicacion), None
    else:
        division = (a / b)
        return float(suma), float(resta), float(multiplicacion), float(division)

def calcular_imc(peso, altura):
    '''Ejercicio 8: Función que recibe el peso en kilogramos
y la altura en metros como parámetros, y devuelva el índice de masa corporal (IMC = peso / altura^2).'''
    imc = round(peso / altura**2, 2)
    return imc

def celsius_a_fahrenheit():
    '''Ejercicio 9: Función que recibe una temperatura en grados Celsius como parámetro y devuelve su equivalente en Fahrenheit
(F = C * 9 / 5 + 32).'''
    celsius = float(input("-> Ingrese la temperatura en grados Celsius a convertir: "))
    fahrenheit = round((celsius * 9 / 5 +32), 2)
    print(f"La temp. {celsius}ºC es equivalente a {fahrenheit}ºF.")

def calcular_promedio():
    '''Ejercicio 10: función llamada calcular_promedio(a, b, c) que recibe
tres números como parámetros y devuelve su promedio.'''
    print("\n(!) A continuación ingrese los tres números a calcular su promedio: ")
    print("(!) Los números decimales son válidos.")
    num1 = float(input("-> Ingrese el primer número: "))
    num2 = float(input("-> Ingrese el segundo número: "))
    num3 = float(input("-> Ingrese el tercer número: "))
    promedio = round((num1+num2+num3)/3, 2) 
    print(f"\n>> El promedio entre {num1}, {num2} y {num3} es de: {promedio}")