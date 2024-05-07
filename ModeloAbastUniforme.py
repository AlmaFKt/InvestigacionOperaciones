import math

CostoUds= int(input("Costo por unidad($): "))  
D=int(input("Demanda por año(uds): "))  
S=int(input("Tasa de abastecimiento(uds/año): "))  
Co=int(input("Costo por ordenar($): "))  
Ch=int(input("Costo de conservación($/ud/año): ")) 
L=int(input("Tiempo de entrega(días): "))

Q=round(math.sqrt(((2*D)*Co)/(Ch*(1-D/S))))

T=Q/S

Produccion=round(T*365)

Imax=round((S-D)*T)

NoProduccion=round(Imax/(D/365))

CAI=round(((D/Q)*Co)+(Q/2*(1-D/S)*Ch))

R=round((D/365)*L)

print(f"Cantidad optima a ordenar (Q): {Q} uds")
print(f"Periodo para ordenar (t): {T} años")
print(f"Inventario maximo (Imax): {Imax} uds")
print(f"Costo anual de inventario (CAI): ${CAI}")
print(f"Punto de reorden (R): {R} uds")
print(f"Periodo de producción: {Produccion} días")
print(f"Periodo sin produccion: {NoProduccion} días")

