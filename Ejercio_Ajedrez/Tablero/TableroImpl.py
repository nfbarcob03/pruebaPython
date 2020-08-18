import numpy as np
from Tablero.TableroInterfaz import  TableroInterfaz


class TableroImpl(TableroInterfaz):

    tablero = None
    
    def __init__(self): 
        self.tablero = np.zeros((8,8))

    def setTablero(self, tablero): 
        self.tablero = tablero

    def getTablero(self): 
        return self.tablero

    def setPosicion(self, posicion): 
        self.tablero[posicion[0],posicion[1]] = 8

    def getPosicion(self): 
        return np.where(self.tablero == 8)