import os
import re

#####################################
#####################################

FULL_TABLE_NAME = 'SeoulBikeData.csv'

#####################################
#####################################


RELATIVE_PATH = './documents/'
RELATIVE_PATH_COLLECTION = './documents/collections/'


def getTableName():
    TABLE = limpiar_nombre(os.path.splitext(os.path.basename(FULL_TABLE_NAME))[0])
    return TABLE

def limpiar_nombre(nombre):
    # Reemplaza espacios y caracteres especiales con guiones bajos
    return re.sub(r'[^a-zA-Z0-9_]', '_', nombre)
