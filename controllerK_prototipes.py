from databaseController import *
from k_prototipes import *

# definimos el numero de k-protoripes
k = 2

# obteniendo el valor en base de datos de los prototipos
numberPrototipes = getPrototipes(k)

print(numberPrototipes)

prototipes = getDataPrototipes(numberPrototipes)

print(prototipes)

# ejecutar el algoritmo kprototipes

result = controller_Kprototipes(prototipes)

# print(result)