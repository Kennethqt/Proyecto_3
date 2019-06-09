from Carro import *
from Piloto import *
from Pickle import *
class Escuderia:
    
    def __init__(self,nombre,logo,ubicacion,patrocinadores,lista_pilotos,automoviles):
        self.__nombre = nombre
        self.__logo = logo
        self.__ubicacion = ubicacion
        self.__patrocinadores = patrocinadores
        self.__pilotos = lista_pilotos
        self.__automoviles = automoviles
        
    def addPatrocinador(self,newPatrocinador):
        self.__patrocinadores.append(newPatrocinador)
    def getPatrocinadores(self):
        stringsalida=""
        for patrocinador in self.__patrocinadores:
            stringsalida+=" "+patrocinador+"\n"
        return stringsalida
    def getPatrocinadoresLista(self):
        return self.__patrocinadores
    def removePatrocinadores(self,patrocinador):
        lista=[]
        for i in self.__patrocinadores:
            if(i == patrocinador):
                self.__patrocinadores.remove(i)
            else:
                lista.append(i)
        return lista
    def setNombre(self,newNombre):
        self.__nombre = newNombre
    def getNombre(self):
        return self.__nombre
    def setLogo(self,newLogo):
        self.__logo=newLogo
    def getLogo(self):
        return self.__logo
    def setUbicacion(self,newUbicacion):
        self.__ubicacion=newUbicacion
    def getUbicacion(self):
        return self.__ubicacion
    def getPilotos(self):
        return self.__pilotos
    def getAutomoviles(self):
        return self.__automoviles
    def addPiloto(self,newPiloto):
        self.__pilotos.append(newPiloto)    
    def addAutomovil(self,newAutomovil):
        self.__automoviles.append(newAutomovil)



                        
