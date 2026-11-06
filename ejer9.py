# Programa que guarda diez numeros y luego los imprime

numeros = []
for i in range(9):
    print(f"Ingresa un numero en la posición {i}:")
    numero = int(input(">"))
    numeros.append(numero)

print("Lista de nombres:")
print(numeros)
