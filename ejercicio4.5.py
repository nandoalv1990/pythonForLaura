# Programa para practicar métodos

# Este es un método que devuelve un mensaje
def mensaje():
    return "Hola este es un mensaje"

# Este es un método que guarda un mensaje
def guarda(mensaje):
    mensaje = input()
    return mensaje

# Ahora los utilizamos
print(mensaje())

print("Ahora tu guarda un mensaje")

print(f"Tu mensaje es {guarda(mensaje)}")

print("Ahora probemos con numeros!\n")

# Este método es una funcion
def f(x):
    return x**2 + 3

x = float(input("Ingresa el nuevo valor de x:"))

print(f"f({x}) = {x}^2 + 3 --> {f(x)}")