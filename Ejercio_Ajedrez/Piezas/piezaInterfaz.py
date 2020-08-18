import abc
from abc import ABCMeta

class piezaInterfaz(object):
    __metaclass__ = ABCMeta

    @abc.abstractmethod
    def verMovimientos(self, tablero): pass
   