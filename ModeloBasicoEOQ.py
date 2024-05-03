import math

D=int(input("Demanda por año(uds): "))
Co=int(input("Costo de ordenar($): "))
Ch=int(input("Costo de conservación($/ud/año): "))
L=int(input("Tiempo de entrega(días): "))


#Round = Redondeo en decimales
#Cantidad a ordenar(uds)
Q=math.sqrt((2*D*Co)/Ch)
Q = round(Q)
#Costo Anual de Inventario
CAI=(D/Q)*Co + (Q/2)*Ch
CAI = round(CAI)
#Reorden
R=(D/365)*L
R = round(R)
#Demanda diaria
Dd=(D/365)
Dd = round(Dd)
#Periodo de abastecimiento
Tiempo=(Q/Dd)
Tiempo = round(Tiempo)

print(f"Cantidad a ordenar: {Q} uds")
print(f"Costo Anual de Inventario: ${CAI} ")
print(f"Reorden: {R} uds")
print(f"Demanda diaria: {Dd} uds")
print(f"Periodo de abastecimiento: {Tiempo} días")