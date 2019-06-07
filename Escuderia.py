
from Carro import *
from Piloto import *
from Pickle import *
class Escuderia:
        #falta logo
    def __init__(self,nombre,ubicacion,patrocinadores,lista_pilotos,automoviles):
        self.__nombre = nombre
        #self.__logo = logo
        self.__ubicacion = ubicacion
        self.__patrocinadores = patrocinadores
        self.__pilotos = lista_pilotos
        self.__automoviles = automoviles
        
    def addPatrocinador(self,newPatrocinador):
        self.__patrocinadores.append(newPatrocinador)
    def getPatrocinadores(self):
        stringsalida=""
        for patrocinador in self.__patrocinadores:
            stringsalida+=" "+patrocinador
        return stringsalida
    def setNombre(self,newNombre):
        self.__nombre = newNombre
    def getNombre(self):
        return self.__nombre
   # def setLogo(self,newLogo):
    #    self.__logo=newLogo
    #def getLogo(self):
    #    return self.__logo
    def setUbicacion(self,newUbicacion):
        self.__ubicacion=newUbicacion
    def getUbicacion(self):
        return self.__ubicacion
    def getPilotos(self):
        return self.__pilotos
    def getAutomoviles(self):
        autosalida=""
        for auto in self.__automoviles:
            autosalida+=" "+auto
            return autosalida
        return self.__automoviles
    def addPiloto(self,newPiloto):
        self.__pilotos.append(newPiloto)
        
    def addAutomovil(self,newAutomovil):
        self.__automoviles.append(newAutomovil)

