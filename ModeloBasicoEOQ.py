import math

D=int(input("Demanda por año(uds): "))
Co=int(input("Costo de ordenar($): "))
Ch=int(input("Costo de conservación($/ud/año): "))
L=int(input("Tiempo de entrega(días): "))


#Round = Redondeo en decimales
#Cantidad a ordenar(uds)
Q=round(math.sqrt((2*D*Co)/Ch))

#Costo Anual de Inventario
CAI=(D/Q)*Co + (Q/2)*Ch

#Reorden
R=round((D/365)*L)

#Demanda diaria
Dd=round((D/365))

#Periodo de abastecimiento
Tiempo=round((Q/Dd))


print(f"Cantidad a ordenar: {Q} uds")
print(f"Costo Anual de Inventario: ${CAI} ")
print(f"Reorden: {R} uds")
print(f"Demanda diaria: {Dd} uds")
print(f"Periodo de abastecimiento: {Tiempo} días")