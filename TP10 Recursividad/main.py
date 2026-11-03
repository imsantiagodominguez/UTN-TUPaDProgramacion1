print('''¡Bienvenido a mi solución al TP10 - Recursividad!
Alumno: Santiago Dominguez''')
print("_"*70)

from def_func import fact

'''Consigna 1. Se pide crear una función recursiva que calcule el factorial de un número entero no
negativo y utilizarla para calcular y mostrar en pantalla el factorial de todos los números
enteros entre 1 y el número que indique el usuario.'''
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
        print("(ERROR!) << Debe ingresar un valor numérico entero >>")
        
print("_"*70)