import re
import sys

from Mensajes import Mensajes
from Operaciones.OperacionInterfaz import operacionInterfaz

class SumaResta(operacionInterfaz):
    def __init__(self):
        operacionInterfaz.__init__(self)

    def calcular(self, suma):
        suma = suma.replace(" ", "")
        if(re.match(r'\d', suma[0])):
            signo = '+'
            suma = signo+suma
        if((re.match(r'^(((\+|\-)?(\d+))+)$', suma) != None)):
            suma = suma.replace("+", " +")
            suma = suma.replace("-", " -")
            suma = suma.strip()
            listaNumeros = suma.split(' ')
            listaNumeros = list(map(float, listaNumeros))
            resultado =self.sumalista(listaNumeros)
        else:
            resultado = Mensajes.error['patronInvalido']
            
        return resultado

    def sumalista(self, listaNumeros):
        if len(listaNumeros) == 1:
            return listaNumeros[0]
        else:
            return listaNumeros[0] + self.sumalista(listaNumeros[1:])