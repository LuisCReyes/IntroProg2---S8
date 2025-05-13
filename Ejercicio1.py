"""Caso 1: Control de venta de vigorón en feria universitaria UAM
Desarrolle un programa que permita simular la venta de vigorón durante una feria gastronómica
organizada en la Universidad Americana, UAM Managua. El sistema debe solicitar la cantidad
de clientes atendidos y, por cada cliente, cuántas porciones de vigorón compró, junto con el
precio unitario por porción. El programa debe calcular el total pagado por cada cliente y mostrar
el total de ventas de toda la feria. Utilice estructuras cíclicas anidadas."""


clientes_atendidos = int(input("Ingresar la cantidad de clientes atendidos: "))
total_ventas = 0

for cliente in range (clientes_atendidos):
    print(f"\nCliente {cliente + 1}:")
    
    porciones = int(input("Cuantas porciones de vigorón compró?: "))
    
    total_cliente = 0
    
    for porcion in range (porciones):
        precio_unitario = float(input(f"Ingrese el precio unitario de la porción #{porcion + 1}: "))
        total_cliente += precio_unitario
        
    print(f"Total pagado por el cliente {cliente + 1}: C${total_cliente:.2f}")
    
    total_ventas += total_cliente
    
print(f"\nTotal de ventas de toda la feria: C${total_ventas:.2f}")