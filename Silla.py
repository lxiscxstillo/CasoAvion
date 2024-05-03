from enum import Enum

class Clase(Enum):
    EJECUTIVA = 1
    ECONOMICA = 2

class Ubicacion(Enum):
    VENTANA = 1
    CENTRO = 2
    PASILLO = 3

class Silla:
    def __init__(self, pNumero, pClase, pUbicacion):
        self.pNumero = pNumero
        self.pClase = pClase
        self.pUbicacion = pUbicacion
        self.__pasajero = None

    def asignarPasajero(self, pPasajero):
        self.__pasajero = pPasajero

    def desasignarSilla(self):
        self.__pasajero = None

    def sillaAsignada(self):
        if self.__pasajero is None:
            return "la silla esta desocupada"
        else:
            return "la silla esta ocupada"
        
    def darNumero(self):
        return self.pNumero

