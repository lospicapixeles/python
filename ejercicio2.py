def convertir_calificacion(numerica):
    if numerica >= 15:     
        return "A"             # literal "A" para indicar notas de 15 a 20
    elif numerica >= 11:
        return "B"             # literal "A" para indicar notas de 11 a 14
    elif numerica >= 0:
        return "C"             # literal "A" para indicar notas de 0 a 10
    else:
        return "F"


# Función para ingresar y convertir calificaciones en tiempo real
def ingresar_y_convertir():
    while True:
        entrada = input("Ingrese una calificación numérica (o 'salir' para terminar): ")
        if entrada.lower() == 'salir':
            break
        try:
            calificacion = float(entrada)  # Convertir a número
            if 0 <= calificacion <= 100:
                letra = convertir_calificacion(calificacion)
                print(f"Calificación numérica: {calificacion}, Calificación literal: {letra}")
            else:
                print("La calificación debe estar entre 0 y 20.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Ejecutar el proceso de entrada y conversión
ingresar_y_convertir()