import sys
import abc
from abc import ABCMeta
from Piezas.piezaInterfaz import piezaInterfaz

class Alfil(piezaInterfaz):
    def __init__(self):
       piezaInterfaz.__init__(self)

    def verMovimientos(self, tablero):
       posicion = tablero.getPosicion() 
       nuevoTablero  = tablero.getTablero()

       ##movidas de alfil
       anteriorPosicionDerecha=posicion
       anteriorPosicionIzquierda=posicion
       siguientePosicionDerecha=posicion
       siguientePosicionIzquierda=posicion

       for i in range(1, int(posicion[0])+1):
          if((0 <= posicion[0]-i <= nuevoTablero.shape[0]-1) & (0 <= posicion[1]+i <= nuevoTablero.shape[1]-1)):
             anteriorPosicionDerecha = [posicion[0]-i,posicion[1]+i]
             nuevoTablero[tuple(anteriorPosicionDerecha)] = 1
          if((0 <= posicion[0]-i <= nuevoTablero.shape[0]-1) & (0 <= posicion[1]-i <= nuevoTablero.shape[1]-1)):
            anteriorPosicionIzquierda = [posicion[0]-i,posicion[1]-i]
            nuevoTablero[tuple(anteriorPosicionIzquierda)] = 1

       for i in range (nuevoTablero.shape[0] - int(posicion[0])):
          if((0 <= posicion[0]+i <= nuevoTablero.shape[0]-1) & (0 <= posicion[1]-i <= nuevoTablero.shape[1]-1)):
             siguientePosicionDerecha = [posicion[0]+i,posicion[1]-i]
             nuevoTablero[tuple(siguientePosicionDerecha)] = 1
          if((0 <= posicion[0]+i <= nuevoTablero.shape[0]-1) & (0 <= posicion[1]+i <= nuevoTablero.shape[1]-1)):
             siguientePosicionIzquierda = [posicion[0]+i,posicion[1]+i]
             nuevoTablero[tuple(siguientePosicionIzquierda)] = 1

       tablero.setTablero(nuevoTablero)
       tablero.setPosicion(posicion)
       return tablero

