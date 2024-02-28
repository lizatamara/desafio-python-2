import sys
import random


jugador = str(sys.argv[1])

#jugador = input("Ingresa piedra, papel o tijera: ")

opciones = ['piedra', 'papel', 'tijera']

computador = (random.choice(opciones))


if jugador == 'piedra' or jugador == 'tijera' or jugador == 'papel':
    
    print(f"Tu jugaste: {jugador}")
    print(f"El computador jugó: {computador}")
    if jugador == computador:
        print("Es un empate")
    elif jugador == 'piedra' and computador == 'tijera':
        print ("Ganaste")
    elif jugador == 'piedra' and computador == 'papel':
        print ("Perdiste")
    elif jugador == 'tijera' and computador == 'papel':
        print ("Ganaste")
    elif jugador == 'papel' and computador == 'piedra':
        print ("Ganaste")
    else:
        print("Perdiste")
else:
    print('Argumento inválido: Debe ser piedra, papel o tijera')