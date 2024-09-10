# Leer numeros
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

# Crear una lista con los numeros que ingresaron
numeros = [numero1, numero2, numero3]

# Ordenar la lista en orden ascendente
numeros_ordenados = sorted(numeros)

# Imprimir los números ordenados
print("Los números en orden ascendente son:")
for numero in numeros_ordenados:
    print(numero)
