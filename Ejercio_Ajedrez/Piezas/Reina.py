import sys
import abc
from abc import ABCMeta
from Piezas.piezaInterfaz import piezaInterfaz
from Piezas.Torre import Torre
from Piezas.Alfil import Alfil

class Reina(piezaInterfaz):
    def __init__(self):
       piezaInterfaz.__init__(self)

    def verMovimientos(self, tablero):
       posicion = tablero.getPosicion() 
       #nuevoTablero  = tablero.getTablero()
       movimientosTorre = Torre()
       movimientosAlfil = Alfil() 
       
       ##Movidas de torre
       tablero = movimientosTorre.verMovimientos(tablero)

       ##movidas de alfil
       tablero = movimientosAlfil.verMovimientos(tablero)

       tablero.setPosicion(posicion)
       return tablero

