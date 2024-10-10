# NOTA: Acho improvável que isso caia porque depende de uma biblioteca para apresentar classes abstratas

from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass


class FiatUno(Veiculo):
    def acelerar(self):
        print("Acelerando...")


fiat_uno = FiatUno()
fiat_uno.acelerar()
