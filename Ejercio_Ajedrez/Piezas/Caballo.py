import sys
import abc
from abc import ABCMeta
from Piezas.piezaInterfaz import piezaInterfaz


class Caballo(piezaInterfaz):
    def __init__(self):
        piezaInterfaz.__init__(self)

    def verMovimientos(self, tablero):
        posicion = tablero.getPosicion()
        nuevoTablero = tablero.getTablero()

        # movidas rey 
        if(posicion[0][0]+2 <= 7):
            if(posicion[1][0]-2 >= 0):
                nuevoTablero[posicion[0][0] + 1, posicion[1][0] - 2] = 1
                nuevoTablero[posicion[0][0] + 2, posicion[1][0] - 1] = 1
            if(posicion[1][0]+2 <= 7):
                nuevoTablero[posicion[0][0] + 1, posicion[1][0] + 2] = 1
                nuevoTablero[posicion[0][0] + 2, posicion[1][0] + 1] = 1

        if(posicion[0][0]-2 >= 0):
            if(posicion[1][0]-2 >= 0):
                nuevoTablero[posicion[0][0] - 1, posicion[1][0] - 2] = 1
                nuevoTablero[posicion[0][0] - 2, posicion[1][0] - 1] = 1
            if(posicion[1][0]+2 <= 7):
                nuevoTablero[posicion[0][0] - 1, posicion[1][0] + 2] = 1
                nuevoTablero[posicion[0][0] - 2, posicion[1][0] + 1] = 1

        tablero.setTablero(nuevoTablero)
        tablero.setPosicion(posicion)
        return tablero