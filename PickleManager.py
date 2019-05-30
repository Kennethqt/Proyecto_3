import os
import pickle

#TODOS LOS ARCHIVOS TIENEN QUE ESTAR EN LA MISMA CARPETA

def cargarArchivo():
    #Busca si existe el archivo de memoria donde se almacenan los datos
    existe = os.path.isfile("Memory.obj")

    #Si existe, lo carga en memoria para agregar o buscar datos
    if existe:

        print("Archivo de memoria si existe")

        file = open("Memory.obj", "rb")

        memoria = pickle.load(file)

        file.close()

    #Si no existe, lo crea y lo retorna para buscar o agregar datos
    else:

        print("Archivo de memoria no existe")

        file = open("Memory.obj", "wb+")

        memoria = {}

        pickle.dump(memory, file)

        file.close()

    return memoria

def guardarArchivo(memory):
    #Abre el archivo para sobreescribir los datos
    file = open("Memory.obj", "wb")

    pickle.dump(memory, file)

    file.close()


def crearDatos(nombre, cedula, telefono, sexo, edad):
    #Crea un diccionario/json nuevo para agregarlo al de la memoria
    data = {}

    data["nombre"] = nombre
    data["cedula"] = cedula
    data["telefono"] = telefono
    data["sexo"] = sexo
    data["edad"] = edad

    return data

def agregarDatos(memoria,nuevosDatos):
    #Busca si ya existe el numero de cedula que se quiere agregar
    verif = cedulaExisteRecursivo(nuevosDatos["cedula"], memoria,0)

    print(verif)
    #Si el numero de cedula no existe, datos sera False, por lo que se agregan los datos
    if not verif:
        memoria[len(memoria)] = nuevosDatos

    #Si el numero de cedula si existe, se actualizan los datos
    else:
        datos = buscarPorCedulaRecursivo(nuevosDatos["cedula"], memoria,0)
        datos["nombre"] = nuevosDatos["nombre"]
        datos["sexo"] = nuevosDatos["sexo"]
        datos["edad"] = nuevosDatos["edad"]
        datos["telefono"] = nuevosDatos["telefono"]

    #Guarda el archivo inmediatamente despues de agregar datos nuevos
    guardarArchivo(memoria)

    return memoria


#-------------Funciones de busqueda, ambas cumplen el mismo proposito-----------------
def buscarPorCedula(cedula, memoria):

    for i in range(len(memoria)):
        if memoria[i]["cedula"] == cedula:
            return memoria[i]
    return False #Retorna falso si no existe

def buscarPorCedulaRecursivo(cedula, memoria, indice):

    if indice == len(memoria):
        return False #Retorna falso si no existe
    elif cedula == memoria[indice]["cedula"]:
        return memoria[indice]
    else:
        return buscarPorCedulaRecursivo(cedula,memoria,indice+1)

def cedulaExiste(cedula,memoria):
    for i in range(len(memoria)):
        if memoria[i]["cedula"] == cedula:
            return True
    return False #Retorna falso si no existe

def cedulaExisteRecursivo(cedula,memoria,indice):

    if indice == len(memoria):
        return False #Retorna falso si no existe
    elif cedula == memoria[indice]["cedula"]:
        return True
    else:
        return buscarPorCedulaRecursivo(cedula,memoria,indice+1)


#---------------------------------------------------------------------------------------
memoria = cargarArchivo()

data = crearDatos("Eduardo Quiroga","123456", "123456", "M", "20")

memoria = agregarDatos(memoria,data)

print(memoria)
