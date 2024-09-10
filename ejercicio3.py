def RadHexa():
    num = float(input("Ingrese un valor en radianes: "))
    grados = num * 180 / 3.14
    hexa = hex(int(grados))
    print("El valor en hexadecimal es: " + hexa)

def HexaRad():
    hexa = input("Ingrese un valor en hexadecimal: ")
    grados = int(hexa, 16)
    radianes = grados * 3.14 / 180
    print("El valor en radianes es: " + str(radianes))


RadHexa()
HexaRad()

