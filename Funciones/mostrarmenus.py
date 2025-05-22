def mostrar_menu_principal():
    print("""
=============================================
          Simulador de Gasto Diario
=============================================
Seleccione una opción:

1. Registrar nuevo gasto
2. Listar gastos
3. Calcular total de gastos
4. Generar reporte de gastos
5. Salir
=============================================        
""")

def menu_registrar_nuevo_gasto():
    print("""
=============================================
            Registrar Nuevo Gasto
=============================================
Ingrese la información del gasto:

- Monto del gasto:
- Categoría (ej. comida, transporte, entretenimiento, otros):
- Descripción (opcional):

Ingrese 'S' para guardar o 'C' para cancelar.
=============================================      
""")
    
def menu_listar_gastos():
    print("""
=============================================
                Listar Gastos
=============================================
Seleccione una opción para filtrar los gastos:

1. Ver todos los gastos
2. Filtrar por categoría
3. Filtrar por rango de fechas
4. Regresar al menú principal
=============================================       
""")
    
def menu_calcular_total_gastos():
    print("""
=============================================
          Calcular Total de Gastos
=============================================
Seleccione el periodo de cálculo:

1. Calcular total diario
2. Calcular total semanal
3. Calcular total mensual
4. Regresar al menú principal
=============================================      
""")

def menu_generar_reporte_gastos():
    print("""
=============================================
           Generar Reporte de Gastos
=============================================
Seleccione el tipo de reporte:

1. Reporte diario
2. Reporte semanal
3. Reporte mensual
4. Regresar al menú principal
=============================================      
""")
    
def menu_salir_del_programa():
    print("""
=============================================
	        Salir
=============================================
               
""")