from databaseController import *
from k_prototipes import *
from databaseController import *
# clase inicial donde llamamos todo el programa
# definimos el numero de k-prototypes
k = 2

# obteniendo el valor en base de datos de los prototipos
numberPrototipes = getPrototipes(k)

#numberPrototipes = [2, 5, 2]

print(numberPrototipes)

#obteniendo datos de los prototipos
prototipes = getDataPrototipes(numberPrototipes)

print(prototipes)

# ejecutar el algoritmo kprototipes

result = controller_Kprototipes(prototipes)

#readCsv()

# print(result)