
from Carro import *
from Piloto import *

class Escuderia:
        #falta logo
    def __init__(self,nombre,ubicacion,patrocinadores,lista_pilotos,automoviles):
        self.__nombre = nombre
        #self.__logo = logo
        self.__ubicacion = ubicacion
        self.__patrocinadores = patrocinadores
        self.__pilotos = lista_pilotos
        self.__automoviles = automoviles
        self.__escuderias = escuderias
    def addEscuderia(self,newEscuderia):
        self.__escuderias.append(newEscuderia)
    def getEscuderias(self):
        salidaescuderias=[]
        for escuderia in self.__escuderias:
            salidaescuderias+=escuderia
        return salidaescuderias
    def toDiccionario(self):
        dic = {}
        dic["nombre"] = self.__nombre
        dic["ubicacion"] = self.__ubicacion
        dic["patrocinadores"]=self.__patrocinadores

        lista_pilotos = []

        for piloto in self.__pilotos:

            lista_pilotos.append(piloto.toDiccionario())
        
        dic["lista_pilotos"] = lista_pilotos


        automoviles = []

        for automovil in self.__automoviles:
            automoviles.append(automovil.toDiccionario())

        dic["automoviles"] = automoviles

        return dic
        
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
        pilotosalida=""
        for piloto in self.__pilotos:
            pilotosalida+=" "+piloto
            return pilotosalida
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
        
 
