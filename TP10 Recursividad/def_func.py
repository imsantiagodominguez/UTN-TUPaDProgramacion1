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
    
'''Consigna 3. Se pide crear una función recursiva que calcule la potencia de un número base elevado a
un exponente entero no negativo, utilizando la fórmula n^m = n * n^(m - 1), con n^0 = 1 como
caso base. Se pide probar la función en un algoritmo general.'''
def potencia(base, exp):
    if exp == 0:
        return 1
    else:
        return base * potencia(base, exp-1)
    
'''Consigna 4. Se pide crear una función recursiva en Python que reciba un número entero positivo en
base decimal y devuelva su representación en binario como una cadena de texto.
La representación binaria de un número utiliza solamente ceros (0) y unos (1), en base 2.
Para convertir un número decimal a binario, se puede seguir este procedimiento:
1. Dividir el número por 2.
2. Guardar el resto (0 o 1).
3. Repetir el proceso con el cociente hasta que llegue a 0.
4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.'''
def num_bin(num: int):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        cociente = num // 2
        resto = str(num % 2)
        return num_bin(cociente) + resto
    
'''Consigna 5. Se pide implementar una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes y devuelva True si es un palíndromo o False si no lo es. 
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed().'''
def es_palindromo(palabra):
    # Casos Base para cadena vacía ó cadena de un único carácter
    if len(palabra) <= 1:
        return True
    # Comparación de extremos:
    elif palabra[0] != palabra[-1]:
        return False
    # Caso recursivo
    else:
        return es_palindromo(palabra[1:-1])
    
'''Se pide escribir una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
- No se puede convertir el número a cadena de texto.
- Se deben usar operaciones matemáticas (%, //) y recursión.'''
def suma_digitos(n):
    if n < 10:
        return n
    else:
        ultimo_digito = n % 10
        resto_numero = n // 10
        return ultimo_digito + suma_digitos(resto_numero)