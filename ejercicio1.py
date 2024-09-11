# Cálculo de intereses de una cuenta bancaria
def calcular_interes():
    saldo_inicial = float(input("Ingrese el saldo inicial: "))
    tasa_interes = float(input("Ingrese la tasa de interés anual (en porcentaje): ")) / 100
    tiempo = float(input("Ingrese el tiempo en años: "))

    # Fórmula para el cálculo de interés compuesto
    saldo_final = saldo_inicial * (1 + tasa_interes) ** tiempo

    print(f"El saldo final después de {tiempo} años es: {saldo_final:.2f}")

# Ejecutar el cálculo de interés
calcular_interes()
