
class Piloto:

    def __init__(self,nombre,edad,nacionalidad,temporada,competencias,destacadas,
                 fallidas,foto):
        self.__nombre = nombre
        self.__edad = edad
        self.__nacionalidad = nacionalidad
        self.__temporada = temporada
        self.__competencias = competencias
        self.__destacadas = destacadas
        self.__fallidas = fallidas
        self.__foto = foto
    def rendimiento_global(self):
        rgp=int(self.__destacadas)*100/(int(self.__competencias)-int(self.__fallidas))
        
        return round(rgp,2)
    def rendimiento_especifico(self):
        rep=int(self.__destacadas*100)/(int(self.__competencias)-int(self.__fallidas))
        return round(rep,2)
    def indice_ganador_escuderia(self):
        ige=round(int(self.__destacadas)/int(self.__competencias),1)
        return ige
    def getDestacadas(self):
        return self.__destacadas
    def getCompetencias(self):
        return self.__competencias
    def getFallidas(self):
        return self.__fallidas
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
    def getFoto(self):
        return self.__foto
