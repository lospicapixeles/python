# Autor: ANTONY ELIO AYANSI HUISA
# variables.
numero = int(input("Escribe la dimensión del cuadrado:\n"))

# Escribe la primera línea de asteriscos.
for i in range(numero ):
    print("*", end = ' ')

print("")

# Dibuja las partes laterales |.
n = 1
while( n <= numero - 2):
    for k in range(numero):
        if ( k == 0 ):
            print('*', end = ' ')
        elif (k == numero - 1):
            print('*', end = '  ')
        else:
            print('  ', end = '') 
    print("")
    n += 1

# Dibuja el lado de abajo. ___
i = 0
while i < numero:
    print("*", end = ' ') # Un asterisco mas un espacio.
    i += 1                