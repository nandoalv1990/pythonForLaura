# Programa que es una calculadora básica de dos numeros

def sum(numeroP, numeroQ):
    return numeroP + numeroQ

def div(numeroP, numeroQ):
    if (numeroQ != 0):
        return numeroP / numeroQ
    else:
        return "Error de sintaxis"

print("-- Calculadora --\n\tIngresa dos numeros")
numeroP = float(input("Ingresa el primer numero:"))
numeroQ = float(input("Ingresa el segundo numero:"))

print(f"{numeroP} + {numeroQ} = {sum(numeroP,numeroQ)}")

# Fin del programa