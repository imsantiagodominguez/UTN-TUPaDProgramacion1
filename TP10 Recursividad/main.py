print('''¡Bienvenido a mi solución al TP10 - Recursividad!
Alumno: Santiago Dominguez''')
print("_"*70)

from def_func import fact, fibonacci, potencia, num_bin

print("(>) Solución Ejer. 1:\n")

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

print("(>) Solución Ejer. 2:\n")

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

print("(>) Solución Ejer. 3:\n")

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

print("(>) Solución Ejer. 4:\n")

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