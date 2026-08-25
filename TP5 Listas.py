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
print(lista_notas)
print() # por visual
print(f" - El promedio de tus notas es de: {suma_notas/10}") # Se imprime el promedio y se cálcula en la misma línea.
print(f" - La nota más alta ingresada es: {nota_max}")
print(f" - La nota más baja ingresada es: {nota_min}")
print() # por visual