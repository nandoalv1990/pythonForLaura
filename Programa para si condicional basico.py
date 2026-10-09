# Este programa tiene ciclos condicionales

n = [1,2,3,4,5] # Este es un arreglo de numeros
for i in n:
    print(f"numero {i}")

for i  in range(5):
    print(f"Este mensaje se imprime {i}")

for i in range(0,9,2):
    print(f"Imprime numeros pares {i}")

print ("\nTambién se puede con texto")
nombre = "Laura"
for letra in nombre:
    print(letra)

diccionario = {'a':1, 'b':2, 'c':3} # Esta es una lista
for clave, numero in diccionario.items():
    print(f"Clave {clave}\tIndice {numero}")