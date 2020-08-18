from Mensajes import Mensajes

import sys
import numpy as np
import re


class Main:

    def __init__(self):
        self.break_while = 1
        self.tableroConFicha = None
        self.tableroNumerado = None
# diccionario de opciones de los menus
        self.choisesPrincipal = {  # menu principal
            "1": self.suma,
            "2": self.resta,
            #"3": self.multiplicacionPolinomios,
            #"4": self.multiplicacionEscalar,
            #"5": self.evaluacionPolinomio,
            #"6": self.salir
        }

    def run(self):
        print(Mensajes.common['bienvenida'])

        while self.break_while == 1:
            self.mostrarMenuPrincipa()
            opcion = input(Mensajes.common['io'])
            action = self.choisesPrincipal.get(opcion)
            if action:
                action()

            else:
                print(Mensajes.menu1['0'])

    def mostrarMenuPrincipa(self):
        print(Mensajes.menu1['Menu'], Mensajes.common['es'], Mensajes.menu1['1'], Mensajes.common['es'],
              Mensajes.menu1['2'], Mensajes.common['es'], Mensajes.menu1['3'], Mensajes.common['es'], Mensajes.menu1['4'],
              Mensajes.common['es'], Mensajes.menu1['5'], Mensajes.common['es'], Mensajes.menu1['6'], Mensajes.common['es'])

    def suma(self):
        breakSuma = 1
        while(breakSuma == 1):
            suma = input(Mensajes.suma['ingreseSuma'])
            patronValido = re.match(r'(((\+?)+(\d*)+(\s*)+(\+)+(\s*))*)+(\d*)', suma)
            print(patronValido)
            if(patronValido):
                listaNumeros = suma.split('+')
                listaNumeros = list(map(int, listaNumeros))
                print(self.sumalista(listaNumeros))
            else:
                print(Mensajes.error['patronInvalido'])
            
            print(Mensajes.common['es'],Mensajes.suma['opcion1'], Mensajes.common['es'],Mensajes.suma['opcion2'], Mensajes.common['es'],Mensajes.suma['opcion3'])
            decision = input()

            if(decision == '2'):
                self.run()
            if(decision == '3'):
                self.salir()

    def sumalista(self, listaNumeros):
        if len(listaNumeros) == 1:
            return listaNumeros[0]
        else:
            return listaNumeros[0] + self.sumalista(listaNumeros[1:])

    def resta(self):
        breakSuma = 1
        while(breakSuma == 1):
            resta = input(Mensajes.resta['ingreseResta'])
            patronValido = re.match(r'(((\-?)+(\d*)+(\s*)+(\-)+(\s*))*)+(\d*)', resta)
            if(patronValido):
                listaNumeros = resta.split('+')
                listaNumeros = list(map(int, listaNumeros))
                print(self.restalista(listaNumeros))
            else:
                print(Mensajes.error['patronInvalido'])
            
            print(Mensajes.common['es'],Mensajes.resta['opcion1'], Mensajes.common['es'],Mensajes.resta['opcion2'], Mensajes.common['es'],Mensajes.resta['opcion3'])
            decision = input()

            if(decision == '2'):
                self.run()
            if(decision == '3'):
                self.salir()

    def restalista(self, listaNumeros):
        if len(listaNumeros) == 1:
            return listaNumeros[0]
        else:
            return listaNumeros[0] - self.sumalista(listaNumeros[1:])

    def salir(self):
        sys.exit(0)


if __name__ == "__main__":
    Main().run()
