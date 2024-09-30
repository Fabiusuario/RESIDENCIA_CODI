from databaseController import *
from k_prototipes import *
from manageDocuments import csv_to_sqlite, saveDocuments

def init_kprototipes(k_input):
    # clase inicial donde llamamos todo el programa
    
    # leemos los archivos
    dirNumber = csv_to_sqlite()
    
    # definimos el numero de k-prototypes
    k = k_input

    # obteniendo el id random en base de datos de los prototipos
    numberPrototipes = getPrototipes(k)

    #obteniendo datos de los prototipos
    prototipes = getDataPrototipes(numberPrototipes)

    # ejecutar el algoritmo kprototipes

    result = controller_Kprototipes(prototipes, numberPrototipes)
    
    saveDocuments(k, dirNumber, result)
    
    return result