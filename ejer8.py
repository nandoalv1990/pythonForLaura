# Programa que redondea una calificación

import math

def redondear(calificacion):
    entero = math.floor(calificacion)
    decimales = calificacion - entero
    if decimales > 0.5:
        return entero + 1
    else:
        return entero

print("Ingresa la calificación:")
calificacion = float(input())

if (calificacion >= 6):
   resultado = redondear(calificacion)
   print(f"El resultado es: {resultado}")
else:
    print("La calificación es reprobatoria")
