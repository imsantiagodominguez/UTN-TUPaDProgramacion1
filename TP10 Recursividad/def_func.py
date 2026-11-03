'''Consigna 1. Se pide crear una función recursiva que calcule el factorial de un número entero no
negativo y utilizarla para calcular y mostrar en pantalla el factorial de todos los números
enteros entre 1 y el número que indique el usuario.'''

def fact(num: int):
    if num < 0:
        print("(ATENCION!) << El número tiene que ser entero no negativo >>")
        return
    else:
        return 1 if num == 0 else fact(num - 1) * num
    
'''Consigna 2. Se pide crear una función recursiva que calcule el valor de la sucesión de Fibonacci en la
posición indicada. Posteriormente, se pide mostrar la sucesión completa hasta la posición
que especifique el usuario.'''
def fibonacci(pos: int):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    elif pos < 0:
        return fibonacci(pos + 2) - fibonacci(pos + 1)
    else:
        return fibonacci(pos - 1)+fibonacci(pos - 2)