import math

D=int(input("Demanda por año(uds): "))  
Co=int(input("Costo por ordenar($): "))  
Ch=int(input("Costo de conservación($/ud/año): ")) 
Cs=int(input("Costo pot faltante($/ud/año): "))
L=int(input("Tiempo de entrega(días): "))

K=Cs/(Ch+Cs)

Q=round(math.sqrt(((2*D)*(Co))/(Ch*K)))

CAI = (D / Q) * Co + ((Q / 2) * Ch) * (K**2) + ((Q / 2) * Cs) * ((1 - K)**2)

Imax=round(K*Q)

R=round((-((Q-Imax)-((D/365)*L))))

print(f"k: {K}")    
print(f"Cantidad optima a ordenar (Q): {Q} uds")
print(f"Costo anual de inventario (CAI): ${CAI}")
print(f"Inventario maximo (Imax): {Imax} uds")
print(f"Punto de reorden (R): {R} uds")