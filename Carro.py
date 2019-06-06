class Carro:

    def __init__(self,marca,modelo,pais,temporada,num_baterias,can_pilas,
                 estado,consumo,sensores,peso,eficiencia):
        self.__marca = marca
        self.__modelo = modelo
        self.__pais = pais
        #self.__foto = foto
        self.__temporada = temporada
        self.__num_baterias = num_baterias
        self.__can_pilas = can_pilas
        self.__estado = estado
        self.__consumo = consumo
        self.__sensores = sensores
        self.__peso = peso
        self.__eficiencia = eficiencia
    def toDiccionario(self):
        dic = {}
        dic["marca"] = self.__marca
        dic["modelo"] = self.__modelo
        dic["pais"] = self.__pais
        #dic[""] =
        dic["temporada"] = self.__temporada
        dic["num_baterias"] = self.__num_baterias
        dic["can_pilas"] = self.__can_pilas
        dic["estado"] = self.__estado
        dic["consumo"] = self.__consumo
        dic["sensores"] = self.__sensores
        dic["peso"] = self.__peso
        dic["eficiencia"] = self.__eficiencia
        return dic
        
