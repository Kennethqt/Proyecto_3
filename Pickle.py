import pickle
from Piloto import *
from Escuderia import *
# Store data (serialize)
def write_inicial(args):
    
    with open('escuderias.pickle', 'wb+') as handle:
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
    with open('escuderias.pickle', 'rb') as handle:
        unserialized_data = pickle.load(handle)

        handle.close()
    return unserialized_data




