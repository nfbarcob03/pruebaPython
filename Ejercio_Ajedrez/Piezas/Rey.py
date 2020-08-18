import sys
import abc
from abc import ABCMeta
from Piezas.piezaInterfaz import piezaInterfaz


class Rey(piezaInterfaz):
    def __init__(self):
        piezaInterfaz.__init__(self)

    def verMovimientos(self, tablero):
        posicion = tablero.getPosicion()
        nuevoTablero = tablero.getTablero()

        # movidas rey 
        if(posicion[0][0] < 7):
            if(posicion[1][0] > 0):
                nuevoTablero[posicion[0][0] + 1, posicion[1][0] - 1] = 1
                nuevoTablero[posicion[0][0], posicion[1][0] - 1] = 1
            if(posicion[1][0] < 7):
                nuevoTablero[posicion[0][0] + 1, posicion[1][0] + 1] = 1
                nuevoTablero[posicion[0][0], posicion[1][0] + 1] = 1
            nuevoTablero[posicion[0][0] + 1, posicion[1][0]] = 1

        if(posicion[0][0] > 0):
            if(posicion[1][0] > 0):
                nuevoTablero[posicion[0][0] - 1, posicion[1][0] - 1] = 1
                nuevoTablero[posicion[0][0], posicion[1][0] - 1] = 1
            if(posicion[1][0] < 7):
                nuevoTablero[posicion[0][0] - 1, posicion[1][0] + 1] = 1
                nuevoTablero[posicion[0][0], posicion[1][0] + 1] = 1
            nuevoTablero[posicion[0][0] - 1, posicion[1][0]] = 1

        tablero.setTablero(nuevoTablero)
        tablero.setPosicion(posicion)
        return tablero
