import re
import sys

from Mensajes import Mensajes
from Operaciones.OperacionInterfaz import operacionInterfaz
from Operaciones.SumaResta import SumaResta

class MultiplicacionFactores(operacionInterfaz):
    def __init__(self):
        operacionInterfaz.__init__(self)

    def calcular(self, poli):
        poli = poli.replace(" ", "")

        if((re.match(r'^((\()((\+|\-)?(\d+))+(\)))+$', poli) != None)):
            objetoSumaResta = SumaResta()
            poli = poli.replace(")(", " ")
            poli = poli.replace("(", "")
            poli = poli.replace(")", "")
            listaPolinomios = poli.split(' ')
            listaPolinomios = list(map(objetoSumaResta.calcular, listaPolinomios))
            resultado = self.multiplicacion(listaPolinomios)
        else:
            resultado = Mensajes.error['patronInvalido']

        return resultado
    
    def multiplicacion(self, listaPolinomios):
        if len(listaPolinomios) == 1:
            return listaPolinomios[0]
        else:
            return listaPolinomios[0] * self.multiplicacion(listaPolinomios[1:])