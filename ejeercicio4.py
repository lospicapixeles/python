import math

Valor = int(input("Ingresa un número: "))

while Valor <= 0:  # El bucle se ejecuta si el número es 0 o negativo
    print("El número debe ser mayor que 0 para calcular su raíz cuadrada.")
    Valor = int(input("Ingresa un número nuevamente: "))

# Aquí ya tenemos un número positivo mayor que 0
raiz = math.sqrt(Valor)
print(f"La raíz cuadrada es: {raiz}")