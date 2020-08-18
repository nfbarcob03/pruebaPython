import sys
import abc
from abc import ABCMeta
from Piezas.piezaInterfaz import piezaInterfaz

class Torre(piezaInterfaz):
    def __init__(self):
       piezaInterfaz.__init__(self)

    def verMovimientos(self, tablero):
       posicion = tablero.getPosicion() 
       nuevoTablero  = tablero.getTablero()
       
       ##Movidas de torre
       nuevoTablero[posicion[0],:] = 1
       nuevoTablero[:, posicion[1]] = 1

       tablero.setTablero(nuevoTablero)
       tablero.setPosicion(posicion)
       return tablero

