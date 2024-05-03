class Silla:
    CLASE = {
        'eje':'Ejecutiva',
        'eco':'Economica'
    }

    UBICACION = {
        'ventana':'Ventana',
        'centro':'Centro',
        'pasillo':'Pasillo'
    }

    def __init__(self, pNumero, pClase, pUbicacion):
        # self.__numero = pNumero
        # # Operador ternario 1- pClase es booleano
        # self.__clase = (self.__CLASE['eje'], self.CLASE['eco'])['pClase']
        # # Operador ternario 2
        # # self.__clase = self.CLASE.eco if pClase =='economica' else self.CLASE.eje
        # if pUbicacion == 'ventana':
        #     self.__ubicacion = self.UBICACION['ventana']
        # elif pUbicacion == 'centro':
        #     self.__ubicacion = self.UBICACION['centro']
        # elif pUbicacion == 'pasillo':
        #     self.__ubicacion = self.UBICACION['pasillo']
        # else:
        #     self.__ubicacion = None

        self.__pasajero = None
        self.setNumero(pNumero)
        self.setClase(pClase)
        self.setUbicacion(pUbicacion)

    def asignarPasajero(self, pPasajero):
        self.__pasajero = pPasajero

    def desasignarPasajero(self):
        self.__numero = None
        self.__pasajero = None

    def sillaAsignada(self):

        # return (False, True)[self.__numero is not None]
        return False if self.__numero == None else True
    
    def getNumero(self):
        return self.__numero
    
    def setNumero(self, pNumero):
        self.__numero = pNumero

    def getClase(self):
        return self.__clase
    
    def setClase(self):
        self.__clase = (self.__CLASE['eje'], self.CLASE['eco'])['pClase']

    def getUbicacion(self):
        return self.__ubicacion
    
    def setUbicacion(self, pUbicacion):
        if pUbicacion == 'ventana':
            self.__ubicacion = self.UBICACION['ventana']
        elif pUbicacion == 'centro':
            self.__ubicacion = self.UBICACION['centro']
        elif pUbicacion == 'pasillo':
            self.__ubicacion = self.UBICACION['pasillo']
        else:
            self.__ubicacion = None

    def getPasajero(self):
        return self.__pasajero