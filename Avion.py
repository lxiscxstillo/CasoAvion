from Silla2 import Silla
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

    def contarSillasEjecutivasOcupadas(self):
        contador = 0
        for silla in self.sillasEjecutivas:
            if silla is not None:
                contador += 1
        return contador
    
    def buscarPasajeroEjecutivo(self, pCedula):
        for cedula in self.sillasEjecutivas:
            if cedula == pCedula:
                return "Pasajero ejecutivo encontrado"
            else:
                return None
            
    def buscarSillaEconomicaLibre(self, pUbicacion):
        for ubicacion in self.sillasEconomicas:
            if ubicacion == pUbicacion:
                return "Ubicacion encontrada"
            else:
                return None
            
    def asignarSillaEconomica(self, pUbicacion, pPasajero):
        for silla in self.sillasEconomicas:
            if silla.getUbicacion() == pUbicacion and silla.getPasajero() is None:
                silla.asignarPasajero(pPasajero)
                return True
            else:
                return False
            
    def anularReservaEjecutivo(self, pCedula):
        anulacionExitosa = False
        for silla in self.sillasEjecutivas:
            if Silla.sillaAsignada() and Silla.getPasajero().getCedula() == pCedula:
                Silla.desasignarPasajero()
                anulacionExitosa = True
        return "anulacion exitosa"

            
    def contarVentanasEconomica(self):
        contador = 0
        for Silla in self.sillasEjecutivas:
            if Silla.getUbicacion() == 'Ventana' and Silla.sillaAsignada()==False:
                contador += 1
        return contador

    def hayDosHomonimosEconomica(self):
        for i in range(len(self.sillas_Economicas)):
            silla_i = self.sillas_Economicas[i]
            if silla_i.sillaAsignada():
                nombre_i = silla_i.getPasajero().getNombre()
                for j in range(i + 1, len(self.sillas_Economicas)):
                    silla_j = self.sillas_Economicas[j]
                    if silla_j.sillaAsignada():
                        nombre_j = silla_j.getPasajero().getNombre()
                        if nombre_i == nombre_j:
                            return True
        return False