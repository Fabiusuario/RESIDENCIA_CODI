from databaseController import *
from k_prototipes import *
from databaseController import *

def init_kprototipes(k_input):
    # clase inicial donde llamamos todo el programa
    # definimos el numero de k-prototypes
    k = k_input

    # obteniendo el valor en base de datos de los prototipos
    numberPrototipes = getPrototipes(k)

    #numberPrototipes = [2, 5, 2]

    print(numberPrototipes)

    #obteniendo datos de los prototipos
    prototipes = getDataPrototipes(numberPrototipes)

    print(prototipes)

    # ejecutar el algoritmo kprototipes

    result = controller_Kprototipes(prototipes)

    return result
#readCsv()

# print(result)