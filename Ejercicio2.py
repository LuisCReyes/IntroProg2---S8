""" Caso 2: Registro semanal de gastos de estudiantes UAM
Cree un programa que simule el control de gastos semanales de un grupo de estudiantes de
primer año de la UAM. El sistema debe procesar datos de 4 semanas, y por cada semana,
ingresar el gasto realizado cada día (7 días por semana). El programa debe calcular el total
gastado por semana y el total acumulado del mes. Utilice bucles anidados para recorrer
semanas y días."""

# Definimos la cantidad de semanas y días
semanas = 4
dias = 7
#Total acumulado
total_acumulado = 0
#Gastos por semana
gastos_semanales = []

for semana in range(semanas):
    # Inicializamos el gasto semanal
    gasto_semanal = 0
    print(f"\nSemana {semana + 1}:")
    # Recorremos los días de la semana
    for dia in range(dias):
        # Pedimos el gasto del día
        gasto_dia = float(input(f"Ingrese el gasto del día {dia + 1}: "))
        # Acumulamos el gasto del día al gasto semanal
        gasto_semanal += gasto_dia
    # Agregamos el gasto semanal a la lista de gastos semanales
    gastos_semanales.append(gasto_semanal)
    # Acumulamos el gasto semanal al total acumulado
    total_acumulado += gasto_semanal
    # Mostramos el total gastado en la semana actual
    print(f"Total gastado en la semana #{semana + 1}: C${gasto_semanal}")
    
    #Total gastado en el mes
    print(f"Total acumulado del mes hasta la semana #{semana + 1}: C${total_acumulado}")
