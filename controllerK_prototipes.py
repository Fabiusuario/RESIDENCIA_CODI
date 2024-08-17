from databaseController import *
from k_prototipes import *
from databaseController import *

# definimos el numero de k-protoripes
k = 4

# obteniendo el valor en base de datos de los prototipos
numberPrototipes = getPrototipes(k)

#numberPrototipes = [2, 5, 2]


print(numberPrototipes)

prototipes = getDataPrototipes(numberPrototipes)

print(prototipes)

# ejecutar el algoritmo kprototipes

result = controller_Kprototipes(prototipes)

#readCsv()

# print(result)