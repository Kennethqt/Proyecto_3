class Piloto:

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
    def toDiccionario(self):
         dic = {}
         dic["nombre"] = self.__nombre
         dic["edad"] = self.__edad
         dic["nacionalidad"] = self.__nacionalidad
         dic["temporada"] = self.__temporada
         dic["competencias"] = self.__competencias
         dic["destacadas"] = self.__destacadas
         dic["fallidas"] = self.__fallidas
         dic["victorias"] = self.__victorias
         return dic
