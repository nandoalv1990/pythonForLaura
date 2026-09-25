# Programa con si entonces condicional
deuda = 5500
print(f"Su adeudo es de ${deuda}\nCon cuanto desea abonar?\t")
abono = float(input())
if (abono >= deuda):
    print(f"La deuda ha sido saldada: Cambio ${(deuda-abono)*-1}")
else:
    print(f"Faltan recursos para saldar: ${deuda-abono}")
# Fin del programa