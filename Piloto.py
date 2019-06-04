class Pilotos:

    def __init__(self,nombre,edad,nacionalidad,temporada,competencias,destacadas,
                 fallidas,victorias):
        self.__nombre = nombre
        self.__edad = edad
        self.__nacionalidad = nacionalidad
        self.__temporada = temporada
        self.__competencias = competencias
        self.__destacadas = destacadas
        self.__fallidas = fallidas
        self.__victorias = victorias
    def rendimiento_global(self,v,p,t,a):
        rgp=(v+p)*100/(t-a)
        return rgp
    def rendimiento_especifico(self,v,t,a):
        rep=v*100/(t-a)
        return rep
    def indice_ganador_escuderia(self,v,t):
        ige=v/t
        return ige
