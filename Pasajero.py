class Pasajero:
    def __init__(self, pCedula, pNombre):
        self.__cedula = pCedula
        self.__nombre = pNombre

    def darCedula(self):
        return self.__cedula
    
    def setCedula(self, pCedula):
        self.__cedula = pCedula
    
    def darNombre(self):
        return self.__nombre
    
    def setNombre(self, pNombre):
        self.__nombre = pNombre