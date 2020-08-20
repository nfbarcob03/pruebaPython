from Mensajes import Mensajes
from Operaciones.SumaResta import SumaResta
from Operaciones.MultiplicacionFactores import MultiplicacionFactores
from Operaciones.MultiplicacionPolinomios import MultiplicacionPolinomios
from Operaciones.EvaluacionPolinomios import EvaluacionPolinomios

import sys
import numpy as np
import re



class Main:

    def __init__(self):
        self.break_while = 1

# diccionario de opciones de los menus
        self.choisesPrincipal = {  # menu principal
            "1": self.menuSumaResta,
            "2": self.menuMultiplicacionFactores,
            "3": self.menuMultiplicacionPolinomios,
            "4": self.menuEvaluacionPolinomios,
            # "5": self.evaluacionPolinomio,
            "6": self.salir
        }

        self.choisesOperacion = {  # menu Suma y resta
            "1": 'calcular',
            "2": self.volver,
            "3": self.salir,
  
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

    def menuSumaResta(self):
        self.break_while = 1
        objetoSumaResta = SumaResta()
        suma = input(Mensajes.operaciones['ingreseOperacionSuma'])
        print(objetoSumaResta.calcular(suma))
        while(self.break_while == 1):
            print(Mensajes.common['es'], Mensajes.operaciones['opcion1'], Mensajes.common['es'],
                  Mensajes.operaciones['opcion2'], Mensajes.common['es'], Mensajes.operaciones['opcion3'])
            opcion = input()
            action = self.choisesOperacion.get(opcion)
            if action:
                if opcion == '1':
                    suma = input(Mensajes.operaciones['ingreseOperacionSuma'])
                    print(objetoSumaResta.calcular(suma))
                else:
                    action()
            else:
                print(Mensajes.menu1['0'])
    
    def menuMultiplicacionFactores(self):
        self.break_while = 1
        objetoMultiplicacionFactores = MultiplicacionFactores()
        poli = input(Mensajes.operaciones['ingreseMultiplicacionFactores'])
        print(objetoMultiplicacionFactores.calcular(poli))
        while(self.break_while == 1):
            print(Mensajes.common['es'], Mensajes.operaciones['opcion1'], Mensajes.common['es'],
                  Mensajes.operaciones['opcion2'], Mensajes.common['es'], Mensajes.operaciones['opcion3'])
            opcion = input()
            action = self.choisesOperacion.get(opcion)
            if action:
                if opcion == '1':
                    poli = input(Mensajes.operaciones['ingreseMultiplicacionFactores'])
                    print(objetoMultiplicacionFactores.calcular(poli))
                else:
                    action()
            else:
                print(Mensajes.menu1['0'])

    def menuMultiplicacionPolinomios(self):
        self.break_while = 1
        objetoMultiplicacionPolinomios = MultiplicacionPolinomios()
        poli = input(Mensajes.operaciones['ingreseMultiplicacionPolinomios'])
        print(objetoMultiplicacionPolinomios.calcular(poli))
        while(self.break_while == 1):
            print(Mensajes.common['es'], Mensajes.operaciones['opcion1'], Mensajes.common['es'],
                  Mensajes.operaciones['opcion2'], Mensajes.common['es'], Mensajes.operaciones['opcion3'])
            opcion = input()
            action = self.choisesOperacion.get(opcion)
            if action:
                if opcion == '1':
                    poli = input(Mensajes.operaciones['ingreseMultiplicacionFactores'])
                    print(objetoMultiplicacionPolinomios.calcular(poli))
                else:
                    action()
            else:
                print(Mensajes.menu1['0'])
    
    def menuEvaluacionPolinomios(self):
        self.break_while = 1
        objetoMultiplicacionPolinomios = EvaluacionPolinomios()
        poli = input(Mensajes.operaciones['ingreseMultiplicacionPolinomios'])
        print(objetoMultiplicacionPolinomios.calcular(poli))
        while(self.break_while == 1):
            print(Mensajes.common['es'], Mensajes.operaciones['opcion1'], Mensajes.common['es'],
                  Mensajes.operaciones['opcion2'], Mensajes.common['es'], Mensajes.operaciones['opcion3'])
            opcion = input()
            action = self.choisesOperacion.get(opcion)
            if action:
                if opcion == '1':
                    poli = input(Mensajes.operaciones['ingreseMultiplicacionFactores'])
                    print(objetoMultiplicacionPolinomios.calcular(poli))
                else:
                    action()
            else:
                print(Mensajes.menu1['0'])

    

    def volver(self):
        self.run()

    def salir(self):
        sys.exit(0)


if __name__ == "__main__":
    Main().run()
