from Tablero.TableroInterfaz import TableroInterfaz
from Tablero.TableroImpl import TableroImpl
from Piezas.Reina import Reina
from Piezas.Torre import Torre
from Piezas.Alfil import Alfil
from Piezas.Peon import Peon
from Piezas.Rey import Rey
from Piezas.Caballo import Caballo
from Mensajes import Mensajes

import sys
import numpy as np


class Main:

    def __init__(self):
        self.break_while = 1
        self.tableroConFicha = None
        self.tableroNumerado = None
# diccionario de opciones de los menus
        self.choisesPrincipal = {  # menu principal
            "1": self.setPosicionTableroVacio,
            "2": self.verMovimientosRey,
            "3": self.verMovimientosReina,
            "4": self.verMovimientosAlfil,
            "5": self.verMovimientosTorre,
            "6": self.verMovimientosPeon,
            "7": self.verMovimientosCaballo,
            "8": self.salir
        }

    def run(self):
        print(Mensajes.common['bienvenida'])
        print(Mensajes.common['explicacionTablero'])
        self.tableroNumerado = self.obtenerTableroNumerado()
        print(self.tableroNumerado.getTablero())

        print(Mensajes.common['pedirPosicionFicha'])
        self.tableroConFicha = self.setPosicionTableroVacio()

        print(Mensajes.common['tableroConFichaPuesta'])
        print(self.tableroConFicha.getTablero())
        print(Mensajes.common['separador'])

        print(self.break_while)
        while self.break_while == 1:
            self.mostrarMenuPrincipa()
            opcion = input(Mensajes.common['io'])
            action = self.choisesPrincipal.get(opcion)
            if action:
                if(opcion == '1'):
                    print(self.tableroNumerado.getTablero())
                    self.tableroConFicha = self.setPosicionTableroVacio()
                    tableroRetorno = self.tableroConFicha.getTablero()
                else:
                    tablero = TableroImpl()
                    tablero.setTablero(np.copy(self.tableroConFicha.getTablero()))
                    tableroRetorno = action(tablero).getTablero()
                print(tableroRetorno)
                print(Mensajes.common['separador'])

            else:
                print(Mensajes.menu1['0'])

    def obtenerTableroNumerado(self):
        print(Mensajes.common['tituloTableroNumerado'])
        tableroMuestra = TableroImpl()
        tableroMuestra.setTablero(np.resize(np.arange(64), (8, 8)))
        return tableroMuestra

    def obtenerTableroVacio(self):
        print(Mensajes.common['tituloTableroVacio'])
        tablero = TableroImpl()
        return tablero

    def mostrarMenuPrincipa(self):
        print(Mensajes.menu1['Menu'], Mensajes.common['es'], Mensajes.menu1['1'], Mensajes.common['es'],
              Mensajes.menu1['2'], Mensajes.common['es'], Mensajes.menu1['3'], Mensajes.common['es'], Mensajes.menu1['4'],
              Mensajes.common['es'], Mensajes.menu1['5'], Mensajes.common['es'], Mensajes.menu1['6'], Mensajes.common['es'],
              Mensajes.menu1['7'], Mensajes.common['es'], Mensajes.menu1['8'], Mensajes.common['es'],)

    def setPosicionTableroVacio(self):
        numeroPosicion = input(Mensajes.common['ingresarCasilla'])
        posicion = np.where(self.tableroNumerado.getTablero()
                            == int(numeroPosicion))
        tableroVacio = self.obtenerTableroVacio()
        tableroVacio.setPosicion([posicion[0][0], posicion[1][0]])
        return tableroVacio

    def verMovimientosRey(self, tablero):
        rey = Rey()
        print("------------------------------------Movimientos Peon--------------------------------------")
        return rey.verMovimientos(tablero)

    def verMovimientosPeon(self, tablero):
        peon = Peon()
        print("------------------------------------Movimientos Peon--------------------------------------")
        return peon.verMovimientos(tablero)

    def verMovimientosCaballo(self, tablero):
        caballo = Caballo()
        print("------------------------------------Movimientos Peon--------------------------------------")
        return caballo.verMovimientos(tablero)

    def verMovimientosReina(self, tablero):
        reina = Reina()
        print("------------------------------------Movimientos Reina--------------------------------------")
        return reina.verMovimientos(tablero)

    def verMovimientosAlfil(self, tablero):
        alfil = Alfil()
        print("------------------------------------Movimientos Alfil--------------------------------------")
        return alfil.verMovimientos(tablero)

    def verMovimientosTorre(self, tablero):
        torre = Torre()
        print("-------------------------------------Movimientos Torre-------------------------------------")
        return torre.verMovimientos(tablero)
    

    def salir(self):
        sys.exit(0)


if __name__ == "__main__":
    Main().run()
