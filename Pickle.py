import pickle
import Piloto as Piloto
def ingresar_datos():
    print('Ingresar cedula:')
    ced = int(input())
    print('Ingresar nombre:')
    nombre = input()    
    write(ced,nombre)
# Store data (serialize)
def write_inicial():
    #lista=[]
    #escuderia_inicial= Escuderia()
    #piloto_inicial= Piloto(args)
    #escuderia_inicial.addPiloto(piloto_inicial)
    #lista.append(escuderia_inicial)
    args={1:"Valtteri Bottas",2:"Sebastian Vettel",3:"Pierre Gasly",4:"Nico Hulkenberg",5:"Romain Grosjean",7:"Carlos Sainz",8:"Sergio Perez",9:"Antonio Giovanazzi",10:"Daniil Kvyat",11:"George Rusell"}
    with open('filename.pickle', 'wb') as handle:
        pickle.dump(args, handle, protocol=pickle.HIGHEST_PROTOCOL)
        handle.close()
def write(referencia,nombre):
    list_read=read()
    list_read[referencia]=nombre
    with open('filename.pickle', 'wb') as handle:
        pickle.dump(list_read, handle, protocol=pickle.HIGHEST_PROTOCOL)

        handle.close()

# Load data (deserialize)
def read():
    with open('filename.pickle', 'rb') as handle:
        unserialized_data = pickle.load(handle)

        handle.close()
    return unserialized_data




