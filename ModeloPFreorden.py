import math
import matplotlib.pyplot as plt
import numpy as np

D = int(input("Ingrese la demanda anual (uds): "))  
Co = int(input("Ingrese el costo por ordenar ($): ")) 
Ch = int(input("Ingrese costo de conservación de cada unidad por año: "))  
L = int(input("Ingrese tiempo de entrega (días): ")) 

# Cálculo de las variables del modelo
T = math.sqrt((2 * Co) / (D * Ch))
t = round(365 * T)  
M = round((D * (T + (L / 365))))  
CAI = (Co / T) + ((T * D) / 2) * Ch

# Crear el eje X y Y para la gráfica
periods = 3
x = np.arange(0, periods * t, 1)
y = np.zeros(len(x))

# Rellenar los valores de inventario
for i in range(periods):
    start = i * t
    end = start + t
    y[start:end] = np.linspace(M, 0, end - start)  
    if i < periods - 1:  
        y[end] = M  

# Crear la figura y el eje
fig, ax = plt.subplots()

# Gráfica de la línea de inventario
ax.plot(x, y, label='Nivel de Inventario (M)', color='r')  

# Linea vertical para los puntos de reorden
reorder_points = [L + i * t for i in range(periods)]
for rp in reorder_points:
    ax.axvline(x=rp, color='black', linestyle='--', label=f'Punto de Reorden (L={L} días)' if rp == reorder_points[0] else "",linewidth=1)

# Linea horizontal para el nivel M
ax.axhline(y=M, color='b', linestyle='--', label='Nivel hasta que se ordena',linewidth=1)

#Linea pequeña para indicar el tiempo de entrega
for i in range(periods):
    ax.plot([i * t + t - 1, i * t + t - 1], [0, 0.1 * M], color='black', linestyle='--', linewidth=1)

ax.set_xlabel('Tiempo (días)')
ax.set_ylabel('Nivel de Inventario (M)')
ax.set_title('Modelo de Periodo Fijo de Reorden')
ax.legend()

results_text = f"T (años): {T:.2f}\nt (días): {t}\nM (unidades): {M}\nCAI ($): {CAI:.2f}"
plt.figtext(0.72, 0.75, results_text, bbox={"facecolor":"white", "alpha":0.5, "pad":5}, fontsize=10)

plt.show()