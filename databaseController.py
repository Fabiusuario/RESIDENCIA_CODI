import sqlite3
import random
import pandas as pd
from const import getTableName   
   #metodos para traer y obtener los datos de la bdd
   #random para generar numeros al azar de acuerdo a la longitud de la bdd
    
#abrir bdd
def openDatabase():
    # Conectar a la base de datos 
    conn = sqlite3.connect('database.db')
    
    # Crear un cursor para ejecutar comandos SQL
    cursor = conn.cursor()
    return [cursor, conn]  

#obtenemos prototipos
def getPrototipes(number_prototipes):
    arrDataBase = openDatabase()
    query = f"SELECT count(*) from {getTableName()}"
    arrDataBase[0].execute(query)
    resultados = arrDataBase[0].fetchall()
    prototipes_array = []

    for fila in resultados:
        length = fila[0]
        #arreglo con el numero de k´s que estan definidos
        
    while(int(number_prototipes) != len(prototipes_array)):
        random_number = random.randint(1, length)
        if(random_number not in prototipes_array):
            prototipes_array.append(random_number)
        
    arrDataBase[1].close()
    return prototipes_array

def getDataPrototipes(prototipes):
    arrDataBase = openDatabase()
    query = ""
    resultados = []
    for j in prototipes:
        query = f"SELECT {getHeaderTableSelect()} from {getTableName()} where id = " + str(j)
        arrDataBase[0].execute(query)
        for i in arrDataBase[0].fetchall():
            resultados.append(i)
    arrDataBase[1].close()
    return resultados

def getAllDatabase(discriminate_protoripes):
    arrDataBase = openDatabase()
    query = ""
    resultados = []
    query = f"SELECT {getHeaderTableSelect()} from {getTableName()} where id not in ({getWhereDiscriminate(discriminate_protoripes)})"
    arrDataBase[0].execute(query)
    resultados = arrDataBase[0].fetchall()
    arrDataBase[1].close()
    return resultados

def getHeaderTable():
    arrDataBase = openDatabase()
    arrDataBase[0].execute(f"SELECT {getHeaderTableSelect()} FROM {getTableName()}")
    # Obtener los nombres de las columnas (encabezados)
    encabezados = [descripcion[0] for descripcion in arrDataBase[0].description]
    
    return encabezados

def getHeaderTableSelect():
    arrDataBase = openDatabase()
    headersString = ''
    
    arrDataBase[0].execute(f"SELECT * FROM {getTableName()}")
    # Obtener los nombres de las columnas (encabezados)
    encabezados = [descripcion[0] for descripcion in arrDataBase[0].description]
    
    excluir = {'id'}
    headersString = ', '.join(str(x) for x in encabezados if x not in excluir)
    
    #print(headersString)
    return headersString

def getWhereDiscriminate(discriminate_protoripes):
    headersString = ', '.join(str(x) for x in discriminate_protoripes)
    return headersString

def getIfAlreadyExists():
    arrDataBase = openDatabase()

    # Consulta para verificar si el nombre ya existe
    arrDataBase[0].execute(f"SELECT * FROM tableCount WHERE name = '{getTableName()}' LIMIT 1")
    
    # Verificar si se obtuvo algún resultado
    resultado = arrDataBase[0].fetchone()

    # Cerrar la conexión
    arrDataBase[1].close()

    # Si resultado no es None, el nombre ya existe
    return resultado is not None

def InsertTableName():
    arrDataBase = openDatabase()

    # Consulta para verificar si el nombre ya existe
    arrDataBase[0].execute(f"INSERT INTO tableCount VALUES (null, '{getTableName()}')")

    nuevo_id = arrDataBase[0].lastrowid
    
    arrDataBase[1].commit()
    # Cerrar la conexión
    arrDataBase[1].close()
    
    return nuevo_id

def GetIdTableName():
    arrDataBase = openDatabase()

    # Consulta para verificar si el nombre ya existe
    arrDataBase[0].execute(f"SELECT id from tableCount where name = '{getTableName()}'")

    resultado = arrDataBase[0].fetchone()
    # Cerrar la conexión
    arrDataBase[1].close()
    
    if resultado:
        return resultado[0]
    else:
        return None