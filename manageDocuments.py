import csv
import os
import re
import json
from datetime import datetime
from databaseController import openDatabase, getIfAlreadyExists, InsertTableName, GetIdTableName, getHeaderTable
from const import getTableName, FULL_TABLE_NAME, RELATIVE_PATH, RELATIVE_PATH_COLLECTION

def limpiar_nombre(nombre):
    # Reemplaza espacios y caracteres especiales con guiones bajos
    return re.sub(r'[^a-zA-Z0-9_]', '_', nombre)

def csv_to_sqlite():
    
    # Contador de los directorios
    dirNumber = 0
    
    # Conectar a la base de datos SQLite (si no existe, se creará)
    arrDataBase = openDatabase()

    # Eliminar la tabla existente si ya existe
    arrDataBase[0].execute(f"DROP TABLE IF EXISTS {getTableName()}")
    
    # Abrir el archivo CSV
    with open(RELATIVE_PATH + FULL_TABLE_NAME, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        # Leer el encabezado para obtener los nombres de las columnas
        header = next(reader)
        header = [limpiar_nombre(col) for col in header]  # Limpiar nombres de las columnas

        # Verificar si hay una columna "id" en el encabezado
        tiene_id = any(col.lower() == 'id' for col in header)

        # Si no tiene columna "id", agregar una columna autoincrementable
        if not tiene_id:
            header.insert(0, 'id')
            create_table_query = f"CREATE TABLE IF NOT EXISTS {getTableName()} (id INTEGER PRIMARY KEY AUTOINCREMENT, {', '.join([f'{col} TEXT' for col in header[1:]])})"
        else:
            create_table_query = f"CREATE TABLE IF NOT EXISTS {getTableName()} ({', '.join([f'{col} TEXT' for col in header])})"
        
        arrDataBase[0].execute(create_table_query)

        # Insertar los datos del CSV en la tabla
        if not tiene_id:
            insert_query = f"INSERT INTO {getTableName()} ({', '.join(header[1:])}) VALUES ({', '.join(['?' for _ in header[1:]])})"
        else:
            insert_query = f"INSERT INTO {getTableName()} ({', '.join(header)}) VALUES ({', '.join(['?' for _ in header])})"
        
        # Insertar cada fila de datos
        for row in reader:
            arrDataBase[0].execute(insert_query, row)

    # Confirmar los cambios
    arrDataBase[1].commit()
    
    if(getIfAlreadyExists()):
        print(f"El nombre '{getTableName()}' ya existe en la tabla, no se agrega pero se saca el id.")
        dirNumber = GetIdTableName()

    else:
        print(f"El nombre '{getTableName()}' no existe, se inserta en la tabla y se obtiene el id.")
        dirNumber = InsertTableName()
    # Cerrar la conexión
    arrDataBase[1].close()
    
    return dirNumber
    
def saveDocuments(k, dirNumber, data):
    
    currentDate = datetime.now().strftime("%Y%m%d_%H%M%S")
    ruta_completa = ''
    build_header_table = ''
    countk = 0
    
    buildDir = f'{RELATIVE_PATH_COLLECTION}DATOS_{dirNumber}_{k}_{currentDate}'
    
    if not os.path.exists(buildDir):
        os.makedirs(buildDir)
        
    for header in getHeaderTable():
        build_header_table += f'{header}\t'
                
    for indice, values in enumerate(data):
        ruta_completa = os.path.join(buildDir, f'DATOS_{dirNumber}_{indice}.txt')
        
        with open(ruta_completa, 'w', encoding='utf-8') as archivo:
            
            
            archivo.write("********* prototipes *********\n")
            archivo.write("\n")
            print(values['prototipes'])
            for prototipe in values['prototipes']:
                archivo.write(f'\nk{countk} : \n')
                archivo.write(build_header_table + "\n")
                for tupla in prototipe:
                    archivo.write(tupla + "\t")
                archivo.write("\n")
                countk = countk + 1


            archivo.write("********* collection *********")
            archivo.write("")
            for clave_col, valor_col in values['collection'].items():
                archivo.write('\n'+clave_col + ' : \n')
                for data_tupla in valor_col:
                    archivo.write("\n")
                    archivo.write(build_header_table + "\n")
                    for single_value_tupa in data_tupla:
                        if single_value_tupa is None:
                            archivo.write(f'null\t')
                        else:
                            archivo.write(f'{single_value_tupa}\t')
                    archivo.write("\n")
                
            # # archivo.write(prototipes['collection'])


