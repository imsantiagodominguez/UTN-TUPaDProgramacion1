print('''¡Bienvenido a mi solución al TP10 - Recursividad!
Alumno: Santiago Dominguez''')
print("_"*70)

from def_func import fact, fibonacci, potencia, num_bin, es_palindromo, suma_digitos

print("(>) Solución Ejer. 1: Factorial hasta 'x' número entero positivo\n")

while True:
    num_entrada = input(">> Ingrese un número entero no negativo: ")
    try:
        limite = int(num_entrada)
        if limite >= 0:
            print(f">> Los factoriales hasta el número {num_entrada} son:")
            for i in range(0, limite+1):
                print(f" >> El factorial de {i} es: {fact(i)}")
            break
        else:
            print("(ERROR!) << El número debe ser igual o mayor a 0 para evaluar el rango >>")
    except ValueError:
        print("(ERROR!) << Debe ingresar un número entero positivo >>")
        
print("_"*70)

print("(>) Solución Ejer. 2: Sucesión de Fibonacci hasta 'x' número (admite positivos y negativos)\n")

while True:
    num_pos = input(">> Ingrese un número entero para calcular el valor de la sucesión de Fibnacci hasta esa posición: ")
    try:
        limite = int(num_pos)
        print(f">> Los valores de la sucesión de Fibonacci hasta el número {num_pos} son:")
        paso = 1 if limite >= 0 else -1
        for i in range(0, limite+paso, paso):
            print(f">> Para Fibonacci: ({i}), el valor de la sucesión es: {fibonacci(i)}")
        break
    except ValueError:
        print("(ERROR!) << Debe ingresar un valor numérico entero >>")
    
print("_"*70)

print("(>) Solución Ejer. 3: Potencia no negativa de un número\n")

base = float(input(">> Ingrese el número base de su potencia: "))
while True:
    try:
        exponente = int(input(">> Ingrese el exponente no negativo del núm. base: "))
        if exponente >= 0:
            break
        else:
            print("(ERROR!) << El exponente debe ser un número entero no negativo >>")
    except ValueError:
        print("(ERROR!) << El exponente debe ser un número entero no negativo >>")


print(potencia(base, exponente))

print("_"*70)

print("(>) Solución Ejer. 4: Representación binaria de un número entero positivo\n")

while True:
    try:
        binario = int(input(">> Ingrese el número a convertir a su representación binaria, debe ser entero y positivo: "))
        if binario >= 0:
            break
        else:
            print("(ERROR!) << El número a convertir deber ser un número positivo >>")
    except ValueError:
        print("(ERROR!) << El número a convertir debe ser un número positivo >>")

print(num_bin(binario))

print("_"*70)

print("(>) Solución Ejer. 5: ¿'x' palabra es palíndromo?\n")

while True:
    palabra = (input(">> Ingrese una palabra: "))
    if palabra.isalpha() and palabra.isascii():
        break
    else:
        print("(ERROR!) << Debe ingresar únicamente letras >>")

soy_palindromo = es_palindromo(palabra)

if soy_palindromo == True:
    print(f''' >> VERDADERO, la palabra "{palabra.title()}" es palíndromo.''')
else:
    print(f''' >> FALSO, la palabra "{palabra.title()}" no es palíndromo.''')

print("_"*70)

print("(>) Solución Ejer. 6: Suma de dígitos\n")

while True:
    try:
        num = int(input('''>> Ingrese el número a sumar todos sus dígitos (Ejemplo: 1234 = 10): '''))
        if num < 0:
            print("(ERROR!) << Debe ser un número entero y positivo (num > 0) >>")
        else:
            break
    except ValueError:
        print("(ERROR!) << Se espera un número entero y positivo (num > 0) >>")

print(f''' >> Siendo "{num}", la suma de sus dígitos es:''', suma_digitos(num))

print("_"*70)