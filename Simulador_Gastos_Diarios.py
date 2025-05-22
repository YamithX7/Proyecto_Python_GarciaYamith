from Funciones.mostrarmenus import*
from Funciones.json import*
import time 
from datetime import datetime, timedelta
ListaGastos = abrirJSON()
while True:
    mostrar_menu_principal()
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("\nDebe ingresar un numero entero.")
        time.sleep(1)
        continue

    if opcion in (1,2,3,4,5):

        if opcion == 1:
            menu_registrar_nuevo_gasto()
            cantidad = int(input("¿Cuantos gastos desea registrar? "))
            print("")
            if cantidad < 1:
                print("La cantidad debe ser de al menos 1.")
            for i in range(cantidad):
                print(f"Gasto # {i+1}\n")
                monto = float(input("Ingrese el monto del gasto: "))
                print("")
                categoria = input("Escriba la categoria del gasto:\n"
                "\nComida \nTransporte \nEntretenimientos \nOtros\n \n ")
                print("")
                unidades = int(input("De cuantas unidades fue el gasto: "))
                print("")
                descripcion = input("Descripcion del gasto: (opcional): ")
                print("")
                dicRegistroNuevoGasto = {
                    "Monto": monto,
                    "Categoria": categoria,
                    "Unidades": unidades,
                    "Descripcion": descripcion,
                    "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                confirmacion = input("Introduzca 'S' para guardar o 'C' para cancelar: ").upper()
                if confirmacion == "S":
                    ListaGastos.append(dicRegistroNuevoGasto)
                    guardarJSON(ListaGastos)
                    print("Gasto nuevo guardado")
                elif confirmacion == "C":
                    print("\nGasto cancelado")
                    time.sleep(1)
                    print("\nRegresando al menu principal...")
                    time.sleep(1)
                else:
                    print("\nOpcion no valida.")
                    time.sleep(1)
                    break
                print("")

        elif opcion == 2:
            while True:
                menu_listar_gastos()
                try:
                    filtrarGastos = int(input("Seleccione una opción para filtrar los gastos: "))
                    print("")
                except ValueError:
                    print("\nDebe ingresar un número válido.")
                    time.sleep(1)
                    continue

                if filtrarGastos == 1:
                    if not ListaGastos:
                        print("No hay gastos registrados.")
                    else:
                        for gasto in ListaGastos:
                            print(gasto)
                            input("\nPresione Enter para volver al menú de listado de gastos...")
                            continue  # 
                elif filtrarGastos == 2:
                    categoria_buscada = input("Ingrese la categoría a filtrar: ").capitalize().strip()
                    print(f"\n--- Gastos en la categoría: {categoria_buscada} ---\n")
                    encontrados = False
                    for gasto in ListaGastos:
                        if gasto["Categoria"].capitalize() == categoria_buscada:
                            print(gasto)
                            encontrados = True
                    if not encontrados:
                        print("No se encontraron gastos en esa categoría.")
                    input("\nPresione Enter para continuar...")
                elif filtrarGastos == 3:
                    try:
                        fecha_inicio = input("Ingrese la fecha de inicio (formato YYYY-MM-DD): ").strip()
                        fecha_fin = input("Ingrese la fecha de fin (formato YYYY-MM-DD): ").strip()
                        dt_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
                        dt_fin = datetime.strptime(fecha_fin, "%H:%M:%S")
                        print("\n--- Gastos en el rango de fechas ---\n")
                        encontrados = False
                        for gasto in ListaGastos:
                            fecha_gasto = datetime.strptime(gasto["Fecha"], "%Y-%m-%d %H:%M:%S")
                            if dt_inicio <= fecha_gasto <= dt_fin:
                                print(gasto)
                                encontrados = True
                        if not encontrados:
                            print("No se encontraron gastos en ese rango de fechas.")
                    except ValueError:
                        print("Formato de fecha inválido. Use YYYY-MM-DD.")
                        input("\nPresione Enter para continuar...")
                elif filtrarGastos == 4:
                    print("\nRegresando al menu principal...")
                    time.sleep(1)
                    break
                else:
                    print("")
                    print("¡Ingrese una opción válida!")
                    time.sleep(1)
                    continue

        elif opcion == 3:
            while True:
                menu_calcular_total_gastos()
                try:
                    periodoCalculo = int(input("Seleccione el periodo de cálculo: "))
                except ValueError:
                    print("\nIngrese un número válido.")
                    time.sleep(1)
                    continue

                if periodoCalculo == 1:
                    try:
                        fecha = input("Ingrese la fecha (YYYY-MM-DD): ").strip()
                        fecha_obj = datetime.strptime(fecha, "%Y-%m-%d").date()
                        total = sum(float(g["Monto"]) for g in ListaGastos if datetime.strptime(g["Fecha"], "%Y-%m-%d %H:%M:%S").date() == fecha_obj)
                        print(f"\nTotal de gastos para {fecha}: ${total:.2f}")
                    except ValueError:
                        print("Formato de fecha inválido.")
                        input("\nPresione Enter para continuar...")
                elif periodoCalculo == 2:
                    try:
                        fecha = input("Ingrese una fecha de referencia (YYYY-MM-DD): ").strip()
                        fecha_obj = datetime.strptime(fecha, "%Y-%m-%d").date()
                        inicio_semana = fecha_obj
                        fin_semana = inicio_semana + timedelta(days=6)
                        total = sum(
            float(g["Monto"]) for g in ListaGastos
            if inicio_semana <= datetime.strptime(g["Fecha"], "%Y-%m-%d %H:%M:%S").date() <= fin_semana
        )
                        print(f"\nTotal de gastos del {inicio_semana} al {fin_semana}: ${total:.2f}")
                    except ValueError:
                        print("Formato de fecha inválido.")
                        input("\nPresione Enter para continuar...")
                elif periodoCalculo == 3:
                    try:
                        año = int(input("Ingrese el año (YYYY): ").strip())
                        mes = int(input("Ingrese el número de mes (1-12): ").strip())
                        total = sum(
            float(g["Monto"]) for g in ListaGastos
            if datetime.strptime(g["Fecha"], "%Y-%m-%d %H:%M:%S").year == año and
               datetime.strptime(g["Fecha"], "%Y-%m-%d %H:%M:%S").month == mes
        )
                        print(f"\nTotal de gastos en {año}-{mes:02d}: ${total:.2f}")
                    except ValueError:
                        print("Entrada inválida.")
                        input("\nPresione Enter para continuar...")
                elif periodoCalculo == 4:
                    print("\nRegresando al menu principal...")
                    time.sleep(1)
                    break
                else:
                    print("\n¡Ingrese una opción válida!")
                    time.sleep(1)
                    continue
                

        elif opcion == 4:
            while True:
                menu_generar_reporte_gastos()
                try:
                    tipoReporte = int(input("Seleccione el tipo de reporte: "))
                except ValueError:
                    print("\nIngrese un numero valido")
                    time.sleep(1)
                    continue

                if tipoReporte == 1:
                    try:
                        fecha = input("Ingrese la fecha (YYYY-MM-DD): ").strip()
                        fecha_obj = datetime.strptime(fecha, "%Y-%m-%d").date()
                        gastos_filtrados = [
                        g for g in ListaGastos
                        if datetime.strptime(g["Fecha"], "%Y-%m-%d %H:%M:%S").date() == fecha_obj
        ]
                        if not gastos_filtrados:
                            print("No se encontraron gastos para esa fecha.")
                        else:
                            print(f"\n--- Reporte Diario para {fecha} ---\n")
                            total = 0
                            for g in gastos_filtrados:
                                print(g)
                                total += float(g["Monto"])
                                print(f"\nTotal del día: ${total:.2f}")
                    except ValueError:
                        print("Formato de fecha inválido.")
                        input("\nPresione Enter para continuar...")
                elif tipoReporte == 2:
                    try:
                        fecha = input("Ingrese una fecha de referencia (YYYY-MM-DD): ").strip()
                        inicio_semana = datetime.strptime(fecha, "%Y-%m-%d").date()
                        fin_semana = inicio_semana + timedelta(days=6)
                        gastos_filtrados = [
                        g for g in ListaGastos
                        if inicio_semana <= datetime.strptime(g["Fecha"], "%Y-%m-%d %H:%M:%S").date() <= fin_semana]
                        if not gastos_filtrados:
                            print("No se encontraron gastos en esta semana.")
                        else:
                            print(f"\n--- Reporte Semanal del {inicio_semana} al {fin_semana} ---\n")
                            total = 0
                            for g in gastos_filtrados:
                                print(g)
                                total += float(g["Monto"])
                                print(f"\nTotal semanal: ${total:.2f}")
                    except ValueError:
                        print("Formato inválido.")
                        input("\nPresione Enter para continuar...")
                elif tipoReporte == 3:
                    try:
                        año = int(input("Ingrese el año (YYYY): ").strip())
                        mes = int(input("Ingrese el número del mes (1-12): ").strip())
                        gastos_filtrados = [
                        g for g in ListaGastos
                        if datetime.strptime(g["Fecha"], "%Y-%m-%d %H:%M:%S").year == año and
                            datetime.strptime(g["Fecha"], "%Y-%m-%d %H:%M:%S").month == mes]
                        if not gastos_filtrados:
                            print("No se encontraron gastos en este mes.")
                        else:
                            print(f"\n--- Reporte Mensual para {año}-{mes:02d} ---\n")
                            total = 0
                            for g in gastos_filtrados:
                                print(g)
                                total += float(g["Monto"])
                                print(f"\nTotal mensual: ${total:.2f}")
                    except ValueError:
                        print("Entrada inválida.")
                        input("\nPresione Enter para continuar...")
                elif tipoReporte == 4:
                    print("\nRegresando al menu principal...")
                    time.sleep(1)
                    break
                else:
                    print("")
                    print("\n¡Ingrese una opción válida!\n")
                    time.sleep(1)
                    continue
                

        elif opcion == 5:
            while True:
                menu_salir_del_programa()
                try:
                    salir = input("¿Desea salir del programa? (S/N): ").lower().strip()
                except ValueError:
                    print("Ingrese una opcion valida")
                    time.sleep(1)
                    continue

                if salir == "s": #Sale del programa
                    print("\nSaliendo del programa...\n")
                    time.sleep(1)
                    exit()
                elif salir == "n": #Regresa al menu principal
                    print("\nRegresando al menu principal...")
                    time.sleep(1)
                    continue
                else:
                    print("\n¡Ingrese una opción válida!")
                    time.sleep(1)


    else:
        print("\n¡Ingrese una opción válida!\n")
        time.sleep(1)