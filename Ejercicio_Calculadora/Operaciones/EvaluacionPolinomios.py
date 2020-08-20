import re
import sys
import numpy as np
from operator import methodcaller
from Mensajes import Mensajes
from Operaciones.OperacionInterfaz import operacionInterfaz
from Operaciones.MultiplicacionPolinomios import MultiplicacionPolinomios


class EvaluacionPolinomios(operacionInterfaz):
    def __init__(self):
        operacionInterfaz.__init__(self)

    def calcular(self, ecuacion):
        ecuacion = ecuacion.replace(' ', '')

        if((re.match(r'^((\[)(((((\+|\-)?(\d+))+)(\,{1}))*(((\+|\-)?(\d+))+))(\]))*[x](\=)(\d*)$', ecuacion) != None)):
            ecuacion = ecuacion.split('x')

            poli = ecuacion[0]
            x = float(ecuacion[1].replace('=', ''))
            objetoMultiplicacionPolinomio = MultiplicacionPolinomios()
            lista= objetoMultiplicacionPolinomio.calcular(poli)
            print(lista)
            resultado = 0
            for i in range(len(lista)):
                resultado += lista[i]*(x**(i))

        else:
            resultado = Mensajes.error['patronInvalido']

        return resultado
