# Trabajo Practico Integrador realizado por Santiago Dominguez (43.813.977)


# Ejercicio 1— “Caja del Kiosco”

nombre = input("Ingrese el nombre del cliente: ") # Se solicita ingresar el nombre del cliente, validando su formato.
while not nombre.isalpha() or nombre == "":
    print("Error!\nEl nombre debe contener solo letras y no puede estar vacío.")
    nombre = input("Ingrese el nombre del cliente: ")

compras = input("Ingrese la cantidad de productos a comprar: ") # Se solicita ingresar la cantidad de productos a comprar, validando su formato.
while not compras.isdigit() or compras == "" or int(compras) <= 0:
    print("Error!\nLa cantidad debe ser un nro. entero positivo y no puede estar vacío.")
    compras = input("Ingrese la cantidad de productos a comprar: ")
    
contador = 0 # Variable autilizar como contador en el bucle for.
precioEntero = 0 # Variable para almacenar dato.
precioCdesc = 0.1 # Variable para calcular descuento .
totalSdescuento = 0 # Variable que va acumulando la suma de los precios SIN Descuento.
totalCdescuento = 0.0 # Variable que va acumulando la suma de los precios CON descuento.
ahorro = 0.0 # Variable para almacenar lo ahorrado en total.
promedioXprod = 0.0 # Variable para almacenar el calculo de promedio de $ por producto.

for contador in range (int(compras)):
    precio = input(f"Ingrese el precio del producto Nº {contador + 1}: ") # Se solicita ingresar el precio del prodcuto, validando su formato, y enseñando por pantalla el nro. de producto.
    while not precio.isdigit() or precio == "" or int(precio) < 0:
        print("Error!\nEl precio debe ser un nro. entero mayor que igual 0 y no puede estar vacío.")
        precio = input(f"Ingrese el precio del producto Nº {contador + 1}: ")
    totalSdescuento += int(precio) # Se acumula en la variable este precio ingresado.
    descuento = input("¿Este producto tiene descuento?, responda con 's' o 'n': ").lower() # Se consulta si el producto poseé descuento a aplicar.
    while descuento not in ["s", "n"]: # Se valida el formato del dato ingresado por el usuario.
        print("Error!\nDebe responder con 's' en caso de tener descuento o con 'n' en lo contrario.")
        descuento = input("¿Este producto tiene descuento?, responda con 's' o 'n': ").lower()
    if descuento == "s": # En caso de que ingrese 's', tiene descuento por lo que se aplica el descuento y se suma al totalCdescuento.
        precioEntero = int(precio)
        totalCdescuento += precioEntero - (precioEntero*precioCdesc)
    else: # De lo contrario se suma el precio del producto sin descuento y se acumula también en totalCdescuento.
        precioEntero = int(precio)
        totalCdescuento += precioEntero
            
ahorro = totalSdescuento - totalCdescuento # Se calcúla lo ahorrado por los descuentos.
promedioXprod = totalCdescuento / int(compras) # Se calcúla el promedio de precio por producto.
# Y finalmente se muestra por pantalla el total con descuento, total sin descuento, lo ahorrado y el promedio de precio x producto.
print(f"Total sin descuento = ${totalSdescuento}")
print(f"Total con descuento = ${totalCdescuento}")
print(f"Ahorro total = ${ahorro}")
print(f"Promedio por producto: ${promedioXprod:.2f}")


# Ejercicio 2 — “Acceso al Campus y Menú Seguro”

usuario_correcto = "alumno" # Variable para usuario correcto
clave_correcta = "python123" # Variable para clave correcta

for intento in range(1, 4):
    print("\n--- Acceso al Campus ---")
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    if usuario == usuario_correcto and clave == clave_correcta: # Se valida si el usuario y la clave ingresados son correctos.
        print("Acceso concedido.")
        print("-"*35)
        print("¡Bienvenido!")
        while True: # Bucle para mostrar el menú de acciones hasta que el usuario decida salir.
            print("Menú de acciones:")
            print("1. Ver estado de inscripción")
            print("2. Cambiar clave")
            print("3. Mostrar mensaje motivacional")
            print("4. Salir")

            opcion = input("Seleccione una opción (1-4): ") # Se solicita ingresar la opción deseada, validando su formato.
            if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
                print("Error: Debe ingresar un número entre 1 y 4.")
                continue

            opcion = int(opcion) # Se convierte la opción ingresada a entero para poder compararla en las siguientes condiciones.

            if opcion == 1: # Se muestra el estado de inscripción.
                print("-"*35)
                print("Estado de inscripción: Inscripto")
                print("-"*35)
            elif opcion == 2: # Se solicita cambiar la clave, validando su formato y confirmando que las claves coincidan.
                print("-"*35)
                nueva_clave = input("Ingrese la nueva clave (mínimo 6 caracteres): ")
                if len(nueva_clave) < 6: # Se valida que la nueva clave tenga al menos 6 caracteres.
                    print("Error: La nueva clave debe tener al menos 6 caracteres.")
                    print("-"*35)
                    continue
                confirmacion = input("Confirme la nueva clave: ") # Se solicita confirmar la nueva clave ingresada.
                if nueva_clave != confirmacion: # Se valida que la nueva clave y la confirmación coincidan.
                    print("Error: Las claves no coinciden.")
                    print("-"*35)
                    continue
                clave_correcta = nueva_clave # Se actualiza la clave correcta con la nueva clave ingresada.
                print("Clave cambiada exitosamente.")
                print("-"*35)               
            elif opcion == 3: # Se muestra un mensaje motivacional.
                print("-"*35)
                print("Mensaje motivacional:\n-Haz hoy lo que tu futuro agradecerá.")
                print("-"*35)
            elif opcion == 4: # Se sale del sistema.
                print("-"*35)
                print("Saliendo del sistema. ¡Hasta luego!")
                print("-"*35)
                break
        break
    else:
        print(f"Usuario o clave incorrectos. Intento {intento} de 3.")
    if intento == 3:
        print("Cuenta bloqueada.")


##Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)"

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

while True:
    nombreOp = input("Ingrese el nombre del operador (solo letras): ")
    if nombreOp.isalpha():
        break
    else:
        print("Error: El nombre del operador debe contener solo letras.")
print(f"\n¡Bienvenido, {nombreOp.title()}! Ingrese la opción deseada del menú.")
while True:
    print("\n--- Menú ---")
    print("1. Reservar turno")
    print("2. Cancelar turno (por nombre)")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Seleccione una opción (1-5): ")
    if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Error: Debe ingresar un número entre 1 y 5.")
        continue

    opcion = int(opcion)

    if opcion == 1: # Reservar turno
        while True:
            print("\n--- Reservar Turno ---")
            while True:
                dia = input("Seleccione el día para reservar turno (1=Lunes, 2=Martes): ")
                if dia != "1" and dia != "2":
                    print("Error!\nDebe ingresar 1 para Lunes o 2 para Martes.")
                    continue
                else:
                    break
            while True:
                nombrePaciente = input("Ingrese el nombre del paciente (solo letras): ")
                if not nombrePaciente.isalpha() or nombrePaciente == "":
                    print("Error!\nEl nombre del paciente debe contener solo letras.")
                    continue
                else:
                    break
            if dia == "1" and nombrePaciente != lunes1 and nombrePaciente != lunes2 and nombrePaciente != lunes3 and nombrePaciente != lunes4:
                if lunes1 == "":
                    lunes1 = nombrePaciente
                    print(f"1er Turno libre: Turno reservado para {nombrePaciente.title()}.")
                elif lunes2 == "":
                    lunes2 = nombrePaciente
                    print(f"2do Turno libre: Turno reservado para {nombrePaciente.title()}.")
                elif lunes3 == "":
                    lunes3 = nombrePaciente
                    print(f"3er Turno libre: Turno reservado para {nombrePaciente.title()}.")
                elif lunes4 == "":
                    lunes4 = nombrePaciente
                    print(f"4to Turno libre: Turno reservado para {nombrePaciente.title()}.")
                else:
                    print("Ya no hay turnos disponibles para el día Lunes.")
            elif dia == "2" and nombrePaciente != martes1 and nombrePaciente != martes2 and nombrePaciente != martes3:
                if martes1 == "":
                    martes1 = nombrePaciente
                    print(f"1er Turno libre: Turno reservado para {nombrePaciente.title()}.")
                elif martes2 == "":
                    martes2 = nombrePaciente
                    print(f"2do Turno libre: Turno reservado para {nombrePaciente.title()}.")
                elif martes3 == "":
                    martes3 = nombrePaciente
                    print(f"3er Turno libre: Turno reservado para {nombrePaciente.title()}.")
                else:
                    print("Ya no hay turnos disponibles para el día Martes.")
            elif (dia == "1" and (nombrePaciente == lunes1 or nombrePaciente == lunes2 or nombrePaciente == lunes3 or nombrePaciente == lunes4)) or (dia == "2" and (nombrePaciente == martes1 or nombrePaciente == martes2 or nombrePaciente == martes3)):
                print(f"\nATENCIÓN!\nEl paciente {nombrePaciente.title()} ya tiene un turno reservado para ese día, turno duplicado, por lo tanto, no reservado.")
            break
    elif opcion == 2: # Cancelar turno
        while True:
            if lunes1 == "" and lunes2 == "" and lunes3 == "" and lunes4 == "" and martes1 == "" and martes2 == "" and martes3 == "":
                print("No hay turnos reservados para cancelar.")
                break
            else:
                while True:
                    nombrePaciente = input("Ingrese el nombre del paciente del que desea cancelar el turno (solo letras): ")
                    if not nombrePaciente.isalpha() or nombrePaciente == "":
                        print("Error!\nEl nombre del paciente debe contener solo letras.")
                        continue
                    elif nombrePaciente == lunes1:
                        lunes1 = ""
                        print(f"1er Turno de Lunes, reservado a {nombrePaciente.title()} ha sidocancelado.")
                        break
                    elif nombrePaciente == lunes2:
                        lunes2 = ""
                        print(f"2do Turno de Lunes, reservado a {nombrePaciente.title()} ha sido cancelado.")
                        break
                    elif nombrePaciente == lunes3:
                        lunes3 = ""
                        print(f"3er Turno de Lunes, reservado a {nombrePaciente.title()} ha sido cancelado.")
                        break
                    elif nombrePaciente == lunes4:
                        lunes4 = ""
                        print(f"4to Turno de Lunes, reservado a {nombrePaciente.title()} ha sido cancelado.")
                        break
                    elif nombrePaciente == martes1:
                        martes1 = ""
                        print(f"1er Turno de Martes, reservado a {nombrePaciente.title()} ha sido cancelado.")
                        break
                    elif nombrePaciente == martes2:
                        martes2 = ""
                        print(f"2do Turno de Martes, reservado a {nombrePaciente.title()} ha sido cancelado.")
                        break
                    elif nombrePaciente == martes3:
                        martes3 = ""
                        print(f"3er Turno de Martes, reservado a {nombrePaciente.title()} ha sido cancelado.")
                        break
    elif opcion == 3: # Ver agenda del día
        while True:
            dia = input("Seleccione el día para ver la agenda (1=Lunes, 2=Martes): ")
            if dia != "1" and dia != "2":
                print("Error!\nDebe ingresar 1 para Lunes o 2 para Martes.")
                continue
            else:
                if dia == "1":
                    print("\n--- Agenda del día Lunes ---")
                    print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
                    print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
                    print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
                    print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
                elif dia == "2":
                    print("\n--- Agenda del día Martes ---")
                    print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
                    print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
                    print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")
                break
        pass
    elif opcion == 4: # Ver resumen general
        print("\n--- Resumen General ---") #Calcular turnos ocupados y disponibles por día
        turnosOcupadosLunes = 0
        turnosDisponiblesLunes = 0
        if lunes1 != "": # # Contamos turnos ocupados y disponibles para Lunes, si el turno no está vacío, se suma a los ocupados, de lo contrario a los disponibles.
            turnosOcupadosLunes += 1
        else:
            turnosDisponiblesLunes += 1
        if lunes2 != "":
            turnosOcupadosLunes += 1
        else:
            turnosDisponiblesLunes += 1
        if lunes3 != "":
            turnosOcupadosLunes += 1
        else:
            turnosDisponiblesLunes += 1
        if lunes4 != "":
            turnosOcupadosLunes += 1
        else:
            turnosDisponiblesLunes += 1
        print(f"\nEstado de cupos de turno para Lunes:\n{turnosOcupadosLunes} turnos ocupados\n{turnosDisponiblesLunes} turnos disponibles.")
        turnosOcupadosMartes = 0
        turnosDisponiblesMartes = 0
        if martes1 != "": # Contamos turnos ocupados y disponibles para Martes, si el turno no está vacío, se suma a los ocupados, de lo contrario a los disponibles.
            turnosOcupadosMartes += 1
        else:
            turnosDisponiblesMartes += 1
        if martes2 != "":
            turnosOcupadosMartes += 1
        else:
            turnosDisponiblesMartes += 1
        if martes3 != "":
            turnosOcupadosMartes += 1
        else:
            turnosDisponiblesMartes += 1
        print(f"\nEstado de cupos de turno para Martes:\n{turnosOcupadosMartes} turnos ocupados\n{turnosDisponiblesMartes} turnos disponibles.")
        if turnosOcupadosLunes > turnosOcupadosMartes:
            print("Día con más turnos ocupados: Lunes")
        elif turnosOcupadosMartes > turnosOcupadosLunes:
            print("Día con más turnos ocupados: Martes")
        else:
            print("Empate en la cantidad de turnos ocupados entre Lunes y Martes.")
    elif opcion == 5:
        print("Cerrando sistema. ¡Hasta luego!\n")
        break


# Ejercicio 4 — “Escape Room: La Bóveda”

# Constantes del juego.
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
spam = 0

while True:
    nombreAgente = input("Ingrese el nombre del agente (solo letras): ") # Se solicita nombre de Agente al usuario
    if not nombreAgente.isalpha(): # Se valida el formato del nombre de Agente, usamos not .isalpha() para evaluar si lo ingreasado NO son carácteres alfabeticos. En caso de que no, se solicita nuevamente.
        print("Error!\nEl nombre del agente debe contener solo letras.")
    else: # En caso de que sean carácteres alfabeticos, comienza el juego.
        while (energia > 0 and tiempo > 0 and cerraduras_abiertas < 3) and not alarma: # while que validará que el usuario aún tenga energía, tiempo, no tenga 3 cerraduras abiertas y la alarma no este encendida (not(alarma[False]) = True)
            print(f"\nAgente {nombreAgente.title()}, energía: {energia}, tiempo: {tiempo}, cerraduras abiertas: {cerraduras_abiertas}")
            print("--- Menú de acciones ---")
            print("1. Forzar cerradura (costo: -20 energía, -2 tiempo)")
            print("2. Hackear panel (costo: -10 energía, -3 tiempo)")
            print("3. Descansar (costo: +15 energía, -1 tiempo)")
            opcion = input("Seleccione una opción (1-3): ") # Se solicita opción al usuario.
            if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3: # Se valida el número de opcion ingresado. Si no es un dígito O opcion es menor que 1 O opcion es mayor que 3, no ingresa. 
                print("Error!\nDebe ingresar un número entre 1 y 3.")
                continue
            if opcion == "1": # OPCION: Forzar cerradura.
                print("\nForzando cerradura...")
                spam += 1
                energia -= 20
                tiempo -= 2
                if spam == 3: # Si el usuario ingresa 3 veces consecutivas, a la 3ra inclusive, se activa la alarma y la boveda se cierra, pierde.
                    print("¡Alerta! Has intentado forzar la cerradura 3 veces seguidas.\n - La alarma se ha activado y la boveda se ha cerrado -")
                    alarma = True
                    break
                if tiempo <= 0 or energia < 0: # Si al descontar el costo de la opcion, el usuario no tiene tiempo o energía, pierde.
                    print("\nTe has quedado sin energía o sin tiempo.\n - Has perdido. -\n")
                    print(f"Con {energia} energia de sobra.")
                    print(f"Con un tiempo restante de {tiempo}.")
                    print(f"Lograste abrir {cerraduras_abiertas} cerradura(s).")                    
                    break
                if energia <= 40: # Si el usuario tiene 40 entra en riesgo.
                    print("¡CUIDADO!\nTu energía es baja, tenés menos de 40 puntos de energía.")
                    nro = input("Ingrese un número del 1-3 para evaluar el riesgo de la cerradura: ")
                    while not nro.isdigit() or int(nro) < 1 or int(nro) > 3: # Se valida que ingrese un válido para evaluar.
                        print("Error!\nDebe ingresar un número entre 1 y 3.")
                        nro = input("Ingrese un número del 1 al 3 para evaluar el riesgo de la cerradura: ")
                    nroRiesgoTrue= int(nro)
                    if nroRiesgoTrue == 3: # Si el número que ingresa es 3, se activa la alarma.
                        alarma = True
                if alarma == False:
                        print("¡CERRADURA ABIERTA! Lograste abrir una cerradura.")
                        cerraduras_abiertas += 1                   
            if opcion == "2":
                print("\nHackeando panel...")
                spam = 0
                energia -= 10
                tiempo -= 3
                if energia < 0 or tiempo <= 0:
                    print("\nTe has quedado sin energía o sin tiempo.\n\n - Has perdido. -\n")
                    print(f"Con {energia} energia de sobra.")
                    print(f"Con un tiempo restante de {tiempo}.")
                    print(f"Lograste abrir {cerraduras_abiertas} cerradura(s).")
                    break
                for pasos in range (4):
                    print(f"Paso {pasos + 1} de 4: Hackeando...")
                    codigo_parcial += "A"
                    print(f"Código parcial actual: {codigo_parcial}")
                    if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                        cerraduras_abiertas += 1
                        print("Se abre automáticamente la cerradura y se suma al código final.")
                        codigo_parcial = ""
            if opcion == "3":
                spam = 0
                print("\nDescansando...")
                if energia + 15 <= 100:
                    energia += 15
                tiempo -= 1
                if alarma == True:
                    print("¡CUIDADO!\nLa alarma estaba activada, pierdes 10 puntos de energía.")
                    energia -= 10
            if cerraduras_abiertas == 3:
                print("¡Felicidades! Has abierto todas las cerraduras a tiempo.\nLa boveda se abre...\n\n ¡GANASTE!")
                print(f"+Con {energia} energia de sobra.")
                print(f"+Con un tiempo restante de {tiempo}.")
            if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
                print("\n - SISTEMA BLOQUEADO, PIERDES. -")
        break


# Ejercicio 5 — “Escape Room:"La Arena del Gladiador"

# Constantes del juego
critico = 1.5
hpPlayer = 100
hpBoss = 100
potion = 3
damageBase = 15
damageBaseBoss = 12
turnGladiador = True
jugada = 1 # Para imprimir en pantalla que turno de jugada esta el usuario.

print("¡Bienvenido a La Arena del Gladiador!\n")
while True:
    player = input("Ingrese su nombre de Gladiador: ")
    if not player.isalpha() or player == "": # Se valida formato del nombre del jugador.
        print ("Usuario no válido. Solo debe contener letras (sin símbolos ni números).")
        continue
    else: #En caso de ser correcto el formato, comienza el juego.
        print("\n¡COMIENZA EL COMBATE!\nSuerte en el campo de batalla.")
        while hpPlayer > 0 and hpBoss > 0: # Se valida que ambas vidas sean mayores que 0 aún, para seguir el combate, sino no entra y se evalua las HP para definir el ganador.
            print(f"- HP GLADIADOR = [{hpPlayer}]")
            print(f"- HP BOSS = [{hpBoss}]")
            print(f"- Pociones restantes = [{potion}]")
            print('''\n--- Menú de acciones ---
1. Ataque Pesado
2. Ráfaga Veloz
3. Curar''')
            while True:
                print(f"\n-Turno nº{jugada}.")
                accion = input("Ingrese el número de la acción que quiera realizar: ")
                if not accion.isdigit() or accion == "" or int(accion) < 1 or int(accion) > 3: # Se valida que el usuario ingrese una opción correcta.
                    print(" -Ingrese un número de acción válido (1|2|3).\n -No debe contener letras, símbolos ni puede estar vacío.")
                else:
                    break
                
            action = int(accion) # Se almacena la acción ingresada para poder compararla.
                
            if action == 1: # OPCION: Ataque pesado.
                print('''- Realizaste un "Ataque Pesado".''')
                if hpBoss < 20: # Caso de golpe crítico; por jefe en menos de 20 HP (no inclusive).
                    print("¡GOLPE CRÍTICO!")
                    hpBoss -= damageBase * critico
                    print(f"¡Atacaste al enemigo por {damageBase * critico}!")
                    jugada += 1 # Para contabilizar la jugada.
                else: # En caso de NO golpe crítico, se descuenta la HP al enemigo por el ataque Base.
                    hpBoss -= damageBase
                    print(f"¡Atacaste al enemigo por {damageBase}!")
                    jugada += 1 # Para contabilizar la jugada.
            if action == 2: # OPCION: Ráfaga Veloz.
                print('''\n- Realizaste una "Ráfaga Veloz".''')
                for i in range (3): # Usamos FOR para ejecutar las diferentes ráfagas (que son 3 de 5HP x ráfaga).
                    print(f"Golpe Nº {i+1} de la Ráfaga Veloz.")
                    hpBoss -= 5
                    print("Golpe conectado por 5 de daño.")
                jugada += 1 # Para contabilizar la jugada.
            if action == 3 and potion > 0: # OPCION: Curar. En caso de tener pociones, el jugador se cura 30HP y se resta 1 poción restante.
                hpPlayer += 30
                potion -= 1
                jugada += 1 # Para contabilizar la jugada.
            if potion == 0: # En caso de no tener pociones, se imprime por pantalla al jugador y pierde el turno.
                print("¡No quedan pociones!")
                print(" -Pierdes el turno,")
                jugada += 1 # Para contabilizar la jugada.
            hpPlayer -= damageBaseBoss # Turno del enemigo.
            print("\n- ¡El enemigo te atacó por 12 puntos de daño!\n")
        if hpBoss < 0: # Se evalua si la HP del enemigo es menor que 0, si es así, el jugador GANA.
            print(f"¡VICTORIA! {player} ha ganado la batalla.")
        if hpPlayer <= 0: # Se evalua si la HP del jugador es menor que 0, si es así, el jugador PIERDE.
            print(f"DERROTA. Has caído en combate.")
    break