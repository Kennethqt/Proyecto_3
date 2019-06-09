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

    def getMarca(self):
        return self.__marca
    def setMarca(self,newMarca):
        self.__marca = newMarca
    def getModelo(self):
        return self.__modelo
    def setModelo(self,newModelo):
        self.__modelo = newModelo
    def getPais(self):
        return self.__pais
    def setPais(self,newPais):
        self.__pais = newPais
    def getTemporada(self):
        return self.__temporada
    def setTemporada(self,newTemporada):
        self.__temporada = newTemporada
    def getNumBaterias(self):
        return self.__num_baterias
    def setNumBaterias(self,newNumBaterias):
        self.__num_baterias = newNumBaterias
    def getCanPilas(self):
        return self.__can_pilas
    def setCanPilas(self,newCanPilas):
        self.__can_pilas = newCanPilas
    def getEstado(self):
        return self.__estado
    def setEstado(self,newEstado):
        if(newEstado=="Disponible" or newEstado=="Descargado" or newEstado=="En Reparaciones"):
            self.__estado = newEstado
        else:
            return 
    def getConsumo(self):
        return self.__consumo
    def setConsumo(self,newConsumo):
        self.__consumo = newConsumo
    def getSensores(self):
        return self.__sensores
    def setSensores(self,newSensores):
        self.__sensores = newSensores
    def getPeso(self):
        return self.__peso
    def setPeso(self,newPeso):
        self.__peso = newPeso
    def getEficiencia(self):
        return self.__eficiencia
    def setEficiencia(self,newEficiencia):
        self.__eficiencia = newEficiencia
