
class Piloto:

    def __init__(self,nombre,edad,nacionalidad,temporada,competencias,destacadas,
                 fallidas):
        self.__nombre = nombre
        self.__edad = edad
        self.__nacionalidad = nacionalidad
        self.__temporada = temporada
        self.__competencias = competencias
        self.__destacadas = destacadas
        self.__fallidas = fallidas
    def rendimiento_global(self,destacadas,competencias,fallidas):
        rgp=(destacadas)*100/(competencias-fallidas)
        return rgp
    def rendimiento_especifico(self,destacadas,competencias,fallidas):
        rep=destacadas*100/(destacadas-fallidas)
        return rep
    def indice_ganador_escuderia(self,destacadas,competencias):
        ige=destacadas/competencias
        return ige
    def getNombrePiloto(self):
        return self.__nombre
    def getEdad(self):
        return self.__edad
    def getNacionalidad(self):
        return self.__nacionalidad
    def getTemporada(self):
        return self.__temporada
    def setNombre(self,newName):
        self.__nombre = newName
    def setEdad(self,newAge):
        self.__edad = newAge
    def setNacionalidad(self,newNationality):
        self.__nacionalidad = newNationality
    def setTemporada(self,newSeason):
        self.__temporada = newSeason
    def getCompetencias(self):
        return self.__competencias
    def getDestacadas(self):
        return self.__destacadas
    def getFallidas(self):
        return self.__fallidas
        
