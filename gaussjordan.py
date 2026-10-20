# Metodo Gauss - Jordan
# 2x + 4y - z = 5
# -x + 3y + 2z = 12
# 3x - y + z = 2

import numpy as np

# Matriz
MA = np.array([
    [2.0,4.0,-1.0,5.0],
    [-1.0,3.0,2.0,12.0],
    [3.0,-1.0,1.0,2.0]
    ])

def g_j(matriz):
    M = matriz.copy()
    filas, columnas = M.shape

    for i in range(filas):
        pivote = M[i,i]
        if pivote == 0:
            raise ValueError("El pivore es cero, intercambia las filas.")
        M[i] = M[i] / pivote
        for j in range(filas):
            if i != j:
                factor = M[j,i]
                M[j] = M[j] - factor * M[i]
    return M

matriz_escalonada = g_j(MA)

solucion = matriz_escalonada[:, -1]

x, y, z = solucion
print("Solución:")
print(f"x = {x:.2f}")
print(f"y = {y:.2f}")
print(f"z = {z:.2f}")

# Metodo alterno

ma = np.array([
    [ 2,  4, -1],
    [-1,  3,  2],
    [ 3, -1,  1]
])

e = np.array([5, 12, 2])

x, y, z = np.linalg.solve(ma, e)

print("\nMetodo alterno:")
print(f"x = {x:.2f}\n y = {y:.2f}\n z = {z:.2f}")