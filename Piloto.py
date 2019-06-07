
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

    def getNombre(self):
        return self.__nombre
        
