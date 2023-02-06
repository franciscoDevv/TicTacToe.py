import os
from time import sleep
import numpy as np
from termcolor import colored
import random

def computerChooses(grid):
    aux = False
    while aux != True:
        i = random.randint(1, 3)
        j = random.randint(1, 3)
        if grid[i-1, j-1] != 'X':
            grid[i-1, j-1] = 'O'
            aux = True
def main():
    grid1 = np.array([["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]])
    grid = np.asmatrix(grid1)
    os.system("clear")
    print(colored("Bienvenido a tres en raya", "red"))
    sleep(0.2)
    print("Seleccione el modo de juego, escoja entre las siguientes opciones.")
    print("1. Jugador contra Jugador")
    print("2. Jugador contra Computadora")
    sleep(0.2)
    gamemode = int(input("Seleccione el modo de juego: "))
    sleep(1.5)
    os.system('cls')
    sleep(2)
    aux = 0
    os.system("clear")
    gameFinished = False
    turn = 1
    tie = False
    if gamemode == 1: #jugador contra jugador
        while not gameFinished:
            for i in grid:
                print(*i)

            sleep(1)
            print("En que posición te gustaría hacer un movimiento?")
            a = int(input("Fila: "))
            b = int(input("Columna: "))

            if a > 3 or b > 3:
                print("¡No puedes hacer un movimiento ahí!")
                sleep(2)
                os.system('cls')
                continue
            if turn % 2 != 0:
                if(grid[a-1, b-1] == "_"):
                    grid[a-1, b-1] = "X"
                else:
                    print("¡No puedes hacer un movimiento ahí!")
                    sleep(2)
                    os.system('cls')
                    continue
            elif turn % 2 == 0:
                if(grid[a-1, b-1] == "_"):
                    grid[a-1, b-1] = "O"
                else:
                    print("¡No puedes hacer un movimiento ahí!")
                    sleep(2)
                    os.system('cls')
                    continue
                if np.count_nonzero(grid == '_') == 0:
                    sleep(2)
                    os.system('cls')
                    print('¡Es un empate!')
                    print("Te gustaría volver a jugar otra partida? (Ingresar 1 si es que si, 0 si es que no)")
                    option1 = int(input())
                    if option1 == 1:
                        main()
                    else:
                        exit()
            sleep(2)
            os.system('cls')
            sleep(2)
            if grid[0, 0] != '_' and grid[0, 0] == grid[1, 1] == grid[2, 2] or grid[2, 0] != '_' and grid[2, 0] == grid[1, 1] == grid[0,2] or grid[0,0] != '_' and grid[0,0] == grid[0, 1] == grid[0, 2] or grid[1, 0] != '_' and grid[1, 0] == grid[1,1] == grid[1, 2] or grid[2, 0] != '_' and grid[2, 0] == grid[2, 1] == grid[2, 2] or grid[0, 0] != '_' and grid[0,0] == grid[1, 0] == grid[2, 0] or grid[0, 1] != '_' and grid[0, 1] == grid[1, 1] == grid[2, 1] or grid[0,2] != '_' and grid[0,2] == grid[1, 2] == grid[2, 2]:
                gameFinished = True
                turn = turn + 1
                os.system("clear")
            turn = turn + 1
    else: #jugador contra computadora
        while gameFinished == False:
            for i in grid:
                print(*i)
            sleep(0.2)
            player = 'X'
            print("Es tu turno")
            sleep(0.5)
            print("¿En que posición te gustaría hacer un movimiento?")
            a = int(input("Fila: "))
            b = int(input("Columna: "))
            sleep(0.3)
            if a > 3 or b > 3:
                print("¡No puedes hacer un movimiento ahí!")
                sleep(2)
                os.system('cls')
                continue

            if(grid[a-1, b-1] == "_"):
                grid[a-1, b-1] = player
            else:
                print("¡No puedes hacer un movimiento ahí!")
                sleep(1)
                os.system('cls')
                continue
            if grid[0, 0] != '_' and grid[0, 0] == grid[1, 1] == grid[2, 2] or grid[2, 0] != '_' and grid[2, 0] == grid[1, 1] == grid[0,2] or grid[0,0] != '_' and grid[0,0] == grid[0, 1] == grid[0, 2] or grid[1, 0] != '_' and grid[1, 0] == grid[1,1] == grid[1, 2] or grid[2, 0] != '_' and grid[2, 0] == grid[2, 1] == grid[2, 2] or grid[0, 0] != '_' and grid[0,0] == grid[1, 0] == grid[2, 0] or grid[0, 1] != '_' and grid[0, 1] == grid[1, 1] == grid[2, 1] or grid[0,2] != '_' and grid[0,2] == grid[1, 2] == grid[2, 2]:
                sleep(1)
                os.system('cls')
                for i in grid:
                    print(*i)
                print("¡Has ganado!")
                sleep(1.5)
                os.system('cls')
                print("¿Te gustaría volver a jugar?, marca 1 para volver a jugar y dos para salir del juego.")
                option2 = int(input("Opcion: "))
                if option2 == 1:
                    main()
                else:
                    sleep(1)
                    print("Gracias por jugar")
                    os.system('cls')
                    sleep(1)
                    exit()
                os.system("clear")
            if np.count_nonzero(grid == '_') == 0:
                sleep(2)
                os.system('cls')
                print('¡Es un empate!')
                print("Te gustaría volver a jugar otra partida? (Ingresar 1 si es que si, 0 si es que no)")
                option1 = int(input())
                if option1 == 1:
                    main()
                else:
                    exit()
            os.system('cls')
            sleep(1)
            for i in grid:
                print(*i)
            sleep(2)
            os.system('cls')
            # computadora hace movimiento:
            print("Turno de la computadora")
            computerChooses(grid)
            print(". . .")
            sleep(1)
            print("La computadora ya hizo su movimiento")
            if grid[0, 0] != '_' and grid[0, 0] == grid[1, 1] == grid[2, 2] or grid[2, 0] != '_' and grid[2, 0] == grid[1, 1] == grid[0,2] or grid[0,0] != '_' and grid[0,0] == grid[0, 1] == grid[0, 2] or grid[1, 0] != '_' and grid[1, 0] == grid[1,1] == grid[1, 2] or grid[2, 0] != '_' and grid[2, 0] == grid[2, 1] == grid[2, 2] or grid[0, 0] != '_' and grid[0,0] == grid[1, 0] == grid[2, 0] or grid[0, 1] != '_' and grid[0, 1] == grid[1, 1] == grid[2, 1] or grid[0,2] != '_' and grid[0,2] == grid[1, 2] == grid[2, 2]:
                for i in grid:
                    print(*i)
                print("La computadora ha ganado")
                sleep(2.5)
                os.system('cls')
                print("¿Quieres volver a jugar? Si es así, marca 1, caso contrario marca 0")
                optio3 = int(input("Opcion: "))
                if optio3 == 1:
                    main()
                else:
                    exit()
            sleep(1)
            sleep(1.5)
            os.system('cls')
    for i in grid:
        print(*i)
    sleep(4)
    

    sleep(4)
    os.system('cls')
    print("Te gustaría volver a jugar otra partida? (Ingresar 1 si es que si, 0 si es que no)")
    option = int(input())
    if option == 1:
        main()
    else:
        exit()
main()
