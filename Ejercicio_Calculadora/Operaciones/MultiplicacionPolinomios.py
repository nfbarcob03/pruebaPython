import re
import sys
import numpy as np
from operator import methodcaller
from Mensajes import Mensajes
from Operaciones.OperacionInterfaz import operacionInterfaz
from Operaciones.SumaResta import SumaResta


class MultiplicacionPolinomios(operacionInterfaz):
    def __init__(self):
        operacionInterfaz.__init__(self)

    def calcular(self, poli):
        poli = poli.replace(' ', '')
        objetoSumaResta  = SumaResta()
        
        if((re.match(r'^((\[)(((((\+|\-)?(\d+))+)(\,{1}))*(((\+|\-)?(\d+))+))(\]))*$', poli) != None)):
            poli = poli.replace('][', ' ')
            poli = poli.replace('[', '')
            poli = poli.replace(']', '')
            poli = poli.split(' ')

            poli = list(map(methodcaller("split", ","), poli))
            lista = [[objetoSumaResta.calcular(i) for i in l] for l in poli]
            while (len(lista) > 1):
                aux = np.convolve(lista.pop(), lista.pop())
                lista = lista + [aux]
            resultado = lista[0]
        else:
            resultado = Mensajes.error['patronInvalido']

        return resultado

