import sys
import abc
from abc import ABCMeta
from Piezas.piezaInterfaz import piezaInterfaz
from Mensajes import Mensajes


class Peon(piezaInterfaz):
    def __init__(self):
        piezaInterfaz.__init__(self)

    def verMovimientos(self, tablero):
        posicion = tablero.getPosicion()
        nuevoTablero = tablero.getTablero()

        # movidas peon
        if(posicion[0][0] == 0):
            print(Mensajes.mensajePeon['coronaJugador2'])
        
        elif(posicion[0][0] < 7):
            if(posicion[1][0] > 0):
                nuevoTablero[posicion[0][0] + 1, posicion[1][0] - 1] = -1
            if(posicion[1][0] < 7):
                nuevoTablero[posicion[0][0] + 1, posicion[1][0] + 1] = -1
            nuevoTablero[posicion[0][0] + 1, posicion[1][0]] = 1

        if(posicion[0][0] == 7):
            print(Mensajes.mensajePeon['coronaJugador1'])

        elif(posicion[0][0] > 0):
            if(posicion[1][0] > 0):
                nuevoTablero[posicion[0][0] - 1, posicion[1][0] - 1] = -2
            if(posicion[1][0] < 7):
                nuevoTablero[posicion[0][0] - 1, posicion[1][0] + 1] = -2
            nuevoTablero[posicion[0][0] - 1, posicion[1][0]] = 2

        if(posicion[0][0] == 1):
            nuevoTablero[posicion[0][0] + 2, posicion[1][0]] = 3

        if(posicion[0][0] == 6):
            nuevoTablero[posicion[0][0] - 2, posicion[1][0]] = 3

        tablero.setTablero(nuevoTablero)
        tablero.setPosicion(posicion)
        return tablero
