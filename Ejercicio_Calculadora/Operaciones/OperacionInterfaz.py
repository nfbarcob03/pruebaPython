import abc
from abc import ABCMeta

class operacionInterfaz(object):
    __metaclass__ = ABCMeta

    @abc.abstractmethod
    def calcular(self, string): pass
   