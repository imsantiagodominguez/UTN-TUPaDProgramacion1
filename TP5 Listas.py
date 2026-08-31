## Resolución de Trabajo Práctico 5 - Listas x Santiago Dominguez
#
#
## Ejercicio 1
## Crear una lista con las notas de 10 estudiantes.
##   - Mostrar la lista completa
##   - Calcular y mostrar el promedio.
##   - Indicar la nota mas alta y la mas baja.
#
#suma_notas = 0.0
#promedio = 0.0
#lista_notas = []
#nota_min = 10.0
#nota_max = 0.0
#
#print("¡Bienvenido!\nA continuación ingrese las notas entre 0.0 y 10.0.\n")
#for i in range(1,11):
#    while True: # Ciclo para la solicitud y validación de notas.
#        nota = input(f"Ingrese la nota Nº {i}: ").replace(',', '.')
#        if not nota.isdigit() or float(nota) < 0 or float(nota) > 10:
#            print("Ingrese una nota valida, entre 0.0 y 10.0.")
#            continue
#        else:
#            nota_valida = float(nota)
#            break
#    if nota_valida < nota_min: # Se verifica que la nota no sea más baja que la anterior ingresada.
#        nota_min = nota_valida
#    if nota_valida > nota_max: # Se verifica que la nota no sea más alta que la anterior ingresada.
#        nota_max = nota_valida
#    suma_notas += nota_valida # Variable donde se acumula las notas ingresadas para luego calcular promedio
#    lista_notas.append(nota_valida)
#
#print() # por visual
#for i in range (len(lista_notas)): # Se muestra la lista completa de notas
#    print(f''' - NOTA "{i+1}": {lista_notas[i]}''')
#print() # por visual
#print(f" - El promedio de tus notas es de: {suma_notas/10}") # Se imprime el promedio y se cálcula en la misma línea.
#print(f" - La nota más alta ingresada es: {nota_max}")
#print(f" - La nota más baja ingresada es: {nota_min}")
#print() # por visual
#
#
## Ejercicio 2
## Pedir al usuario que cargue 5 productos en una lista.
##   - Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
##   - Preguntar al usuario qué producto desea eliminar y actualizar la lista.
#
#lista_productos = []
#
#for i in range (5): # Se solicitan los 5 productos.
#    producto = input(f"Ingrese el producto nº {i+1}: ")
#    lista_productos.append(producto)
#
#lista_ordenada = sorted(lista_productos) # Se ordena la lista de elementos ingresada
#
#print(f"\n - La lista de productos que ingreso es la siguiente:")
#for i in range(len(lista_ordenada)): # Se imprime la lista ingresada ya ordenada
#            print(f'''"{i+1}" {lista_ordenada[i]}''')
#
#eliminar = input(" - ¿Desea eliminar un producto y actualizar la lista? (y/n): ").lower()
#while True:
#    if eliminar != "y" and eliminar != "n":
#        print("Opción NO VÁLIDA...")
#        eliminar = input(" - ¿Desea eliminar un producto y actualizar la lista? (y/n): ").lower()
#        continue
#    else:
#        break
#
#if eliminar == "y":
#    print(f''' - ¿Qué producto desea eliminar de la lista? (1-5)
#{lista_ordenada}
#Siendo: 
# "1" {lista_ordenada[0]}
# "2" {lista_ordenada[1]}
# "3" {lista_ordenada[2]}
# "4" {lista_ordenada[3]}
# "5" {lista_ordenada[4]}''')
#    quiero = input(" >> ")
#    while True:
#        if not quiero.isdigit() or int(quiero) < 1 or int(quiero) > 5:
#            print("Opción NO VÁLIDA...")
#            quiero = input(f''' - ¿Qué producto desea eliminar de la lista? (1-5):
# >> ''')
#            continue
#        else:
#            break
#    if quiero == "1":
#        eliminado = lista_ordenada.pop(0) # Se actualiza el primer elemento por el ingresado.
#        print(f" - La lista de productos actualizada es la siguiente:") # Se imprimer por pantalla la nueva lista.
#        for i in range(len(lista_ordenada)):
#            print(f'''PRODUCTO "{i+1}": {lista_ordenada[i]}''')
#    elif quiero == "2":
#        eliminado = lista_ordenada.pop(1) # Se actualiza el primer elemento por el ingresado.
#        print(f" - La lista de productos actualizada es la siguiente:") # Se imprimer por pantalla la nueva lista.
#        for i in range(len(lista_ordenada)):
#            print(f'''PRODUCTO "{i+1}": {lista_ordenada[i]}''')
#    elif quiero == "3":
#        eliminado = lista_ordenada.pop(2) # Se actualiza el primer elemento por el ingresado.
#        print(f" - La lista de productos actualizada es la siguiente:") # Se imprimer por pantalla la nueva lista.
#        for i in range(len(lista_ordenada)):
#            print(f'''PRODUCTO "{i+1}": {lista_ordenada[i]}''')
#    elif quiero == "4":
#        eliminado = lista_ordenada.pop(3) # Se actualiza el primer elemento por el ingresado.
#        print(f" - La lista de productos actualizada es la siguiente:") # Se imprimer por pantalla la nueva lista.
#        for i in range(len(lista_ordenada)):
#            print(f'''PRODUCTO "{i+1}": {lista_ordenada[i]}''')
#    elif quiero == "5":
#        eliminado = lista_ordenada.pop(4) # Se actualiza el primer elemento por el ingresado.
#        print(f" - La lista de productos actualizada es la siguiente:") # Se imprimer por pantalla la nueva lista.
#        for i in range(len(lista_ordenada)):
#            print(f'''PRODUCTO "{i+1}": {lista_ordenada[i]}''')
#    print(f" - PRODUCTO ELIMINADO: {eliminado}.")
#else:
#    print("\n > NO ELIMINAR.\n - Okey, hasta pronto.")
#
#
##Ejercicio 3
## Generar una lista con 15 números enteros al azar entre 1 y 100.
##   - Crear una lista con los pares y otra con los impares.
##   - Mostrar cuántos números tiene cada lista.
#
#import random
#
#numeros_random = [random.randint(1, 100) for _ in range(15)] # Se genera la lista de 15 números enteros random entre 1 y 100.
#lista_pares = []
#lista_impares = []
#
#for i in numeros_random: # Ciclo para recorrer la lista generada y contabilizar los pares e impares.
#    if i % 2 == 0:
#        lista_pares.append(i)
#    else:
#        lista_impares.append(i)
#
## Se imprime la lista original de números random
#print(f''' - La lista original es:''')
#for i in range(15): 
#    print(f'''Número {i+1} = {numeros_random[i]}''')
## Se imprime la lista de pares
#print(f'''\n - La lista de pares es:''')
#for i in range(len(lista_pares)):
#    print(f'''Número {i+1} = {numeros_random[i]}''')
## Se imprime la lista de impares
#print(f'''\n - La lista de impares es:''')
#for i in range(len(lista_impares)):
#    print(f'''Número {i+1} = {numeros_random[i]}''')
## Ejercicio 4
## Dada una lista con valores repetidos:
##   - Crear una nueva lista sin elementos repetidos.
##   - Mostrar el resultado.
#
#datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
#print(" >> RESULTADO DE LISTA ORIGINAL. ")
#for i in range(len(datos)):
#    print(f'''Valor nº {i+1}: {datos[i]}''')
#
#sin_repetir = [] # Guardamos elementos para luego 
#
## Se recorre la lista original y añaden al final de la vacía aquellos que no esten en ella 
#for i in (datos):
#    if i not in sin_repetir:
#        sin_repetir.append(i)
#
#print(" >> RESULTADO DE LISTA SIN ELEMENTOS REPETIDOS. ")
#for i in range(len(sin_repetir)):
#    print(f'''Valor nº {i+1}: {sin_repetir[i]}''')
#
#
## Ejercicio 5
## Crear una lista con los nombres de 8 estudiantes presentes en clase.
##   - Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
##   - Mostrar la lista final actualizada.
#
#lista_estudiantes_en_clase = []
#
#for i in range(5):
#        while True: # Validación de la entrada, para que sea de tipo caracteres
#            estudiante = input(f"> Ingrese el nombre del {i+1} estudiante: ")
#            if not estudiante.isalpha() or estudiante == "":
#               print("(!) Nombre no válido.")
#               continue
#            else:
#                lista_estudiantes_en_clase.append(estudiante)
#                break
#
#print('''> Pregunta:
#¿Quiere agregar un nuevo estudiante o eliminar uno existente?
#- Ingresar "1" para agregar un nuevo estudiante o "2" para eliminar uno existente.''')
#while True:
#    accion = input("> ")
#    if not accion.isdigit() or int(accion) != 1 and int(accion) != 2: # Validación de acción
#        print("(!) Opción no válida.")
#        print('''- Ingresar "1" para agregar un nuevo estudiante o "2" para eliminar uno existente.''')
#        continue
#    else:
#         accion_validada = int(accion)
#         break
#    
#if accion_validada == 1: # Caso donde el usuario quiera agregar un nuevo estudiante al final de la lista ingresada
#    while True: # Validación de la entrada, para que sea de tipo caracteres
#        estudiante = input(f"> Ingrese el nombre del estudiante que desea agregar: ")
#        if not estudiante.isalpha() or estudiante == "":
#           print("(!) Nombre no válido.")
#           continue
#        else: 
#            lista_estudiantes_en_clase.append(estudiante)
#            for i in range(len(lista_estudiantes_en_clase)): # Se imprime por pantalla la lista ingresada dentro de una estructura repetitiva 
#                print(f"{lista_estudiantes_en_clase[i]}")
#            break
#if accion_validada == 2: # Caso donde el usuario quiera eliminar un estudiante existente en la lista.
#    while True:
#        estudiante_eliminar = input("-> Ingrese el estudiante existente en la lista que quiera eliminar: ") # Solicitud de estudiante a eliminar.
#        for i in range(len(lista_estudiantes_en_clase)): # Se recorre la lista la cantidad de veces según los elementos que contenga
#            if estudiante_eliminar in lista_estudiantes_en_clase: # Si el estudiante ingresado a eliminar esta se borra de ella.
#                lista_estudiantes_en_clase.remove(estudiante_eliminar) # Mediante function .remove()
#                print(f'''> Se ha eliminado el estudiante "{estudiante_eliminar}" de la lista.
#>La lista actualizada es:''')
#                for i in range(len(lista_estudiantes_en_clase)): # Se imprime por pantalla mensaje de que ha sido eliminado y se enseña la lista actualizada.
#                    print(f"{lista_estudiantes_en_clase[i]}")
#                break
#            else:
#                print(f'''> El estudiante ingresado no esta en la lista.''') # Caso donde el estudiante a eliminar ingresado por el usuario no se ha encontrado.
#                break
#
#
## Ejercicio 6
## Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha
## (el último pasa a ser el primero).
#
#lista_7_numeros = []
#primer_elemento = ""
#
#print("Bienvenido, a continuación ingrese los números deseados de la lista.")
#for i in range(7):
#    print(f"-> Ingrese el número {i+1}") # Se imprime que sean números, pero el programa funcionaría con cualquier tipo de elementos (str, int, float, Boolean, listas).
#    num = input("> ")
#    lista_7_numeros.append(num)
#
#print() # Por visual
#
#print(f"-> La lista que ingreso es la siguiente:")
#for i in range(len(lista_7_numeros)):
#    print(f"{lista_7_numeros[i]}")
#
#print() # Por visual
#lista_7_numeros_rotados = lista_7_numeros[-1:] + lista_7_numeros[:-1] # Se utiliza el metodo de Slicing.
#
## Se muestra la lista con los elementos rotados una posición hacia la derecha.
#print(f"-> La lista con los elementos rotados una posición hacia la derecha sería:")
#for i in range(len(lista_7_numeros_rotados)):
#    print(f"{lista_7_numeros_rotados[i]}")
#
#
## Ejercicio 7
## Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de a semana.
##   - Calcular el promedio de las mínimas y el de las máximas.
##   - Mostrar en qué día se registró la mayor amplitud térmica.
#
#lista_temperaturas = []
#filas = 7
#columnas = 2
#
#print("(!) A continuación ingrese las temperaturas de la lista. ")
#for i in range(filas):
#    temperaturas_dias = []
#    print(f"-> Día {i+1}:")
#    for j in range(columnas):
#        while True:
#            temperatura = (input(f"-> Ingrese la temperatura {j+1} de la semana {i+1}:\n> ").replace(',','.'))
#            validacion = temperatura.lstrip('-').replace('.', '', 1)
#            if validacion.isdigit():
#                temperatura_valida = float(temperatura)
#                temperaturas_dias.append(temperatura_valida)
#                break
#            else:
#                print("(!) Temperatura no válida, ingrese la temperatura en formato númerico.")
#    if temperaturas_dias[0] > temperaturas_dias[1]:
#        temperatura_acomodadas = temperaturas_dias[-1:] + temperaturas_dias[:-1]
#        lista_temperaturas.append(temperatura_acomodadas)
#    else:
#        temperatura_acomodadas = temperaturas_dias
#        lista_temperaturas.append(temperatura_acomodadas)
#
#print("\n-> La lista diaria de temperaturas ingresada es:")
#for i in range(filas):
#    temperatura_min = lista_temperaturas[i][0] # Ordenamos las temperaturas minimás en la pos (i) 0, que sería a la izquierda.
#    temperatura_max = lista_temperaturas[i][1] # Ordenamos las temperaturas minimás en la pos (i) 1, que sería a la derecha.
#    print(f"-> Día {i+1}: Mínima {temperatura_min} ºC y Máxima {temperatura_max} ºC.") # Se imprime por pantalla las temperaturas por día con su minima y maxima.
#
## Evaluamos la MAX amplitud térmica.
#amplitudes = []
#for i in range(filas):
#    temp_min = lista_temperaturas[i][0] # Ordenamos las temperaturas minimás en la pos (i) 0, que sería a la izquierda.
#    temp_max = lista_temperaturas[i][1] # Ordenamos las temperaturas máximas en la pos (i) 1, que sería a la derecha.
#    amplitudes.append(temp_max - temp_min) # Calculamos las amplitudes día por día y estas mismas las insertamos en una nueva lista donde se contendran estos datos.
#
#mayor_amplitud = max(amplitudes) # Utilizo function max para buscar el máximo dentro de la lista "amplitudes" generada anteriormente.
#menor_amplitud = min(amplitudes) # Utilizo function min para buscar el mínimo dentro de la lista "amplitudes" generada anteriormente.
#
#if mayor_amplitud == menor_amplitud: # CASO 1: Evaluamos si el máximo coincide con el mínimo en caso de que haya habido siempre la misma amplitud térmica.
#    print(f"\n-> La amplitud térmica fue la misma en todos los días. Fue de {mayor_amplitud}.")
#else:
#    dia_mayor_amplitud = 0 # CASO 2: usamos esta VAR para ir guardando que día fue el que hubo mayor amplitud.
#    for i in range(filas):
#        if amplitudes[i] == mayor_amplitud: # Condición para buscar que día de la semana fue que sucedió esa mayor amplitud.
#            dia_mayor_amplitud = i + 1
#            break
#    print(f"\n-> La mayor amplitud térmica registrada fue de {mayor_amplitud} ºC y fue registrada el día {dia_mayor_amplitud}.")
#
#
## Ejercicio 8
## Crear una matriz con las notas de 5 estudiantes en 3 materias.
##   - Mostrar el promedio de cada estudiante.
##   - Mostrar el promedio de cada materia.
#
#estudiantes = 5
#materias = 3
#
#notas_x_matriz = [] # Lista para guardar las notas de cada estudiante
#suma_materias = [0.0] * materias # Se crea la lista donde se guardará el promedio de cada materia.
#
#for i in range(estudiantes):
#    notas_estudiantes = []
#    suma_notas = 0.0
#
#    print(f"< ESTUDIANTE Nº {i+1} >")
#
#    for j in range(materias):
#        while True:
#            nota = input(f"-> Ingrese la nota de la materia Nº {j+1}: ").replace(',', '.')
#            if not nota.replace('.', '', 1).isdigit() or float(nota) < 0.0 or float(nota) > 10.0:
#                print("(!) Nota no válida. Ingrese una nota del 0.0 al 10.0")
#                continue
#            else:
#                nota_valida = float(nota)
#                notas_estudiantes.append(nota_valida)
#                suma_notas += nota_valida # Acumula las notas del estudiante.
#                suma_materias[j] += nota_valida # Acumula la nota de la matería en el 'j' elemento.
#                break
#    promedio_estudiante = suma_notas/materias
#    print(f"-> Promedio del ESTUDIANTE Nº {i+1} es de: {promedio_estudiante:.2f}\n")
#
#print('''< Promedio de cada materia >''')
#for j in range(materias):
#    promedio_materia = suma_materias[j]/estudiantes
#    print(f"-> Promedio de la MATERIA Nº {j+1} es de: {promedio_materia:.2f}")
#
#
## Ejercicio 9
## Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
##   - Inicializarlo con guiones "-" representando casillas vacías.
##   - Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
##   - Mostrar el tablero después de cada jugada.
#
#tateti = [["-" for _ in range (3)] for _ in range (3)]
#jugador_1 = ""
#jugador_2 = ""
#
#print("> Bienvenido al Ta-Te-Ti.")
#print("< Tablero inicial >")
#for i in range(3):
#    print(f"{tateti[i]}")
#
#while True:
#    jugador = input('''-> ¿Que símbolo desea ser "X" o "O"?:\n> ''').upper()
#    if jugador == "X" or jugador == "O":
#        break
#    else:
#        print('''(!) Símbolo inválido, por favor ingrese uno de los solicitado.''')
#        jugador = input('''-> ¿Que símbolo desea ser "X" o "O"?:\n> ''').upper()
#
#jugadas = 0
#ganador = False
#
#while jugadas < 9 and not ganador:
#    print(f'''\n-> Turno del JUGADOR "{jugador}"''')
#
#    pos_fila = input('''-> Ingrese la fila siendo:
#[0]
#[1]
#[2]
#> ''')
#    pos_columna= input('''-> Ingrese la columna siendo:
#[0][1][2]
#> ''')
#    
#    if not pos_fila.isdigit() and not pos_columna.isdigit() or pos_fila == "" or pos_columna == "" or int(pos_fila) < 0 or int(pos_fila) > 2 or int(pos_columna) < 0 or int(pos_columna) > 2:
#        print("(!) Opción NO VÁLIDA, ingrese lo solcitiado.")
#        continue
#
#    fila=int(pos_fila)
#    columna=int(pos_columna)
#
#    if tateti[fila][columna] != "-":
#        print('''(!) La casilla ya está ocupada, elija otra.''')
#        continue
#    tateti[fila][columna] = jugador
#    jugadas += 1
#
#    print(f'''\n< TABLERO PARCIAL >''')
#    for i in range(3):
#        print(f"{tateti[i]}")
#
#    # Evaluación de CASOS de GANADOR
#    for i in range(3):
#        if tateti[i][0] == tateti [i][1] == tateti[i][2] == jugador:
#            ganador = True
#        if tateti[0][i] == tateti [1][i] == tateti [2][i] == jugador:
#            ganador = True
#    if tateti [0][0] == tateti [1][1] == tateti[2][2] == jugador:
#        ganador = True
#    if tateti [0][2] == tateti [1][1] == tateti[2][0] == jugador:
#        ganador = True
#    if ganador == True:
#        print(f'''\n >> ¡HAY UN GANADOR!
#El jugador ganador es: {jugador}.''')
#    else:
#        if jugador == "X":
#            jugador = "O"
#        else:
#            jugador = "X"
#
#if not ganador:
#    print('''\n >> ¡EMPATE! El tablero esta lleno.''')
#print("\n< RESULTADO DEL TABLERO >")
#for i in range(3):
#        print(f"{tateti[i]}")
#
#
## Ejercicio 10
## Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
##   - Mostrar el total vendido por cada producto.
##   - Mostrar el día con mayores ventas totales.
##   - Indicar cuál fue el producto más vendido en la semana
#
#productos = 4 # Filas
#dias = 7 # Columnas
#lista_ventas = []
#
#for i in range(productos):
#    venta_del_producto = []
#    print()
#    print(f"<< REGISTRO DE VENTAS del PRODUCTO Nº {i+1} >>")
#    for j in range(dias):
#        while True: # Validacion de entrada
#            cant_ventas_producto = input(f"-> Cantidad de ventas el día: {j+1}:\n > ")
#            if not cant_ventas_producto.isdigit() or cant_ventas_producto == "" or int(cant_ventas_producto) < 0:
#                print("(!) Cantidad inválida. Ingrese una cantidad la cantidad en números enteros.")
#                continue
#            else:
#                venta_del_producto.append(int(cant_ventas_producto)) # Se va generando la lista de ventas 7 días(columnas) x cantidad de producto (filas)
#                break
#    lista_ventas.append(venta_del_producto) # Se agrega la lista que contiene los 7 días de ese producto
#print() # Por visual.
#
## Total vendido por cada producto + producto con mayor ventas.
#max_producto = -1
#producto_max_ventas = []
#
#for i in range(productos): # Fila donde se recorre.
#    total_productos = 0 # VAR donde acumularemos cada producto, se reinicia cuando se termina de contabilizar 1 producto los 7 días, para su correcto funcionamiento.
#    for j in range(dias): # Se recorre cada columna de la fila.
#        total_productos += lista_ventas[i][j] # Se acumula cada dato que contenga (i, j)
#    print(f"Producto Nº {i+1}: {total_productos} unidades en total.")
#    if total_productos > max_producto: # Lógica para encontrar el producto con mayor venta en la semana.
#        max_producto = total_productos
#        producto_max_ventas = [i + 1]
#    elif total_productos == max_producto: # Si se EMPATAN con el máximo se forma una lista con estos días.
#        producto_max_ventas.append(i + 1)
#
#print() # Por visual.
#
## Total ventas por día.
#max_ventas = -1
#dia_mayor_ventas = []
#for i in range(dias): # Recorremos cada día de 0 a 6 (7 días).
#    total_ventas = 0 # Acumulador de ventas totales x cada día, se reinicia en cada ciclo de día (i).
#    for j in range(productos): # Recorremos cada producto de ese día de 0 a 3 (4 productos).
#        total_ventas += lista_ventas[j][i]
#    print(f"-> El TOTAL de VENTAS del día {i+1} es de {total_ventas} unidades.")
#    if total_ventas > max_ventas: # Lógica para encontrar el día con mayor venta.
#        max_ventas = total_ventas
#        dia_mayor_ventas = [i+1] # Se va sumando uno para luego mostrar el día real donde hubo mayor total de ventas.
#    elif total_ventas == max_ventas:
#        dia_mayor_ventas.append(i+1) # Agregamos el día a la lista existente
#print()
## Imprimimos el/los día(s) con mayores ventas totales.
#print(f'''-> El DÍA con MAYOR VENTAS fue de {max_ventas} productos.''')
#print("--> Ocurrió en el/los día(s): ", end = "") 
#for i in dia_mayor_ventas:
#    print(f'''{i}''', end = " ") # Por visual se utiliza end para imprimir en la linea anterior
#
## Imprimimos cuál fue el/los producto(s) más vendido en la semana
#print(f'''\n-> El PRODUCTO con MAS VENTAS en la SEMANA es {producto_max_ventas} con {max_producto} unidades.''')
#print("--> Producto(s) más vendido(s): ", end = "")
#for i in producto_max_ventas:
#    print(f'''{i}''', end = " ") # Por visual se utiliza end para imprimir en la linea anterior
#
#
## Ejercicio 11
##  Crear una lista con los nombres de 10 estudiantes.
##   - Solicitar al usuario que ingrese un nombre a buscar.
##   - Indicar si el nombre se encuentra en la lista.
##   - Mostrar la posición en la que aparece.
##   - Si no se encuentra, informar que no está en la lista.
#
#cantidad_estudiantes = 10
#lista_estudiantes = []
#
#for i in range(cantidad_estudiantes): # bucle repetitivo para ingresar los estudiantes a una lista.
#    while True: # bucle While para la validación del formato de los nombres, para que el usuario no ingrese números ni algo vacío.
#        estudiante = input(f'''>> Ingrese el nombre del estudiante Nº{i+1}:\n > ''').title()
#        if estudiante.isalpha() and estudiante != "":
#            lista_estudiantes.append(estudiante)
#            break
#        else:
#            print("(!) Formato de nombre inválido.")
#            continue
#
#print() # Por visual.
#estudiante_buscar = input(">> Ingrese el nombre del estudiante que desea buscar en la lista:\n > ").title() # Se solicita el estudiante a buscar.
#
#if estudiante_buscar in lista_estudiantes: # Caso para cuando el estudiante a buscar se encuentra dentro de la lista.
#    for i in range(len(lista_estudiantes)):
#        if estudiante_buscar == lista_estudiantes[i]: # Si estudiante_buscar es == al elemento que tiene lista en la pos i en ese ciclo, se guarda la posición
#            posicion_encontrada = i+1 # sumandole 1 para que sea el número real.
#            print(f">> ENCONTRADO.\n>> El estudiante a buscar ingresado ({estudiante_buscar}) se encuentra en la posición {posicion_encontrada}.")
#            break
#else:
#    print(">> NO SE ENCONTRÓ.\n>> El estudiante a buscar ingresado no se encuentra en la lista.")


# Ejercicio 12
#  Pedir al usuario que ingrese 8 números enteros y almacenarlos en una lista.
#   - Mostrar la lista original.
#   - Mostrar la lista ordenada de menor a mayor.
#   - Mostrar la lista ordenada de mayor a menor.
#   - Investigar el uso de sorted() y del parámetro reverse.

cantidad_numeros = 8 # VAR para la cantidad de elementos en la lista.
lista_enteros = [] # VAR para almacenar los números.

for i in range(cantidad_numeros): # bucle repetitivo para ingresar los números a una lista.
    while True: # bucle While para la validación del formato de los números enteros.
        numero = input(f'''>> Ingrese el número Nº{i+1}:\n > ''')
        if numero.isdigit() and int(numero) >= 0:
            numero_valido = int(numero) # variable temporal para pasar el valor ingresado ya validado como entero
            lista_enteros.append(numero_valido)
            break
        else:
            print("(!) Vacio ó Número incompatible. Ingrese solo números enteros.")
            continue

print()
print('''>> La lista que ha formado es la siguiente: ''') # Se imprime por pantalla la lista ingresada.
for i in range(len(lista_enteros)):
    if i == len(lista_enteros) - 1: # Utilizo esta condicion para mostrar de una forma más estética la lista.
        print(f"{lista_enteros[i]}.")
    else:
        print(f"{lista_enteros[i]},", end = " ")

lista_enteros_mayor_menor = sorted(lista_enteros, reverse= False) # Como se solicita, investigue sobre el uso de sorted y reverse. 
lista_enteros_menor_mayor = sorted(lista_enteros, reverse = True) # En el caso de menor a mayor, se solicita que lo haga en reverse, por eso "reverse = True" 

print()
print('''>> La lista que ha formado ORDENADA de MAYOR A MENOR es la siguiente: ''') # Se imprime por pantalla la lista ingresada ordenada de mayor a menor.
for i in range(len(lista_enteros_mayor_menor)): # Utilizo esta condicion para mostrar de una forma más estética la lista.
    if i == len(lista_enteros_mayor_menor) - 1:
        print(f"{lista_enteros_mayor_menor[i]}.")
    else:
        print(f"{lista_enteros_mayor_menor[i]},", end = " ")

print()
print('''>> La lista que ha formado ORDENADA de MENOR A MAYOR es la siguiente: ''') # Se imprime por pantalla la lista ingresada ordenada de menor a mayor.
for i in range(len(lista_enteros_menor_mayor)): # Utilizo esta condicion para mostrar de una forma más estética la lista.
    if i == len(lista_enteros_menor_mayor) - 1:
        print(f"{lista_enteros_menor_mayor[i]}.")
    else:
        print(f"{lista_enteros_menor_mayor[i]},", end = " ")