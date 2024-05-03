from Silla import Silla
class Avion:
    SILLAS_EJECUTIVAS = 8
    SILLAS_ECONOMICAS = 42

    def __init__(self):
        self.sillasEjecutivas=[]
        self.sillasEconomicas=[]

        self.asignacionSillasEjecutivas()

    def asignacionSillasEjecutivas(self):
        for i in range(self.SILLAS_EJECUTIVAS):
            if ((i+1)%2)==0:
                self.sillasEjecutivas.append(Silla((i+1), False, 'pasillo'))
            else:
                self.sillasEjecutivas.append(Silla((i+1), False, 'ventana'))
    
    def asignacionSillasEconomicas(self):
        for i in range(self.SILLAS_ECONOMICAS):
            if ((i+1)%3)==0:
                self.sillasEconomicas.append(Silla((i+1), False, 'pasillo'))
            elif ((i+1)%3)==1:
                self.sillasEconomicas.append(Silla((i+1), False, 'ventana'))
            else:
                self.sillasEconomicas.append(Silla((i+1), False, 'centro'))