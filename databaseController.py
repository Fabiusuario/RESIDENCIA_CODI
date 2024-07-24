import sqlite3
import random
    
def openDatabase():
    # Conectar a la base de datos (se creará si no existe)
    conn = sqlite3.connect('database.db')
    
    # Crear un cursor para ejecutar comandos SQL
    cursor = conn.cursor()
    return [cursor, conn]
    

def getPrototipes(number_prototipes):
    arrDataBase = openDatabase()
    query = "SELECT count(*) from celulares"
    arrDataBase[0].execute(query)
    resultados = arrDataBase[0].fetchall()
    prototipes_array = []

    for fila in resultados:
        length = fila[0]
        
    for i in range(int(number_prototipes)):
        prototipes_array.append(random.randint(1, length))

    arrDataBase[1].close()
    return prototipes_array

def getDataPrototipes(prototipes):
    arrDataBase = openDatabase()
    query = ""
    resultados = []
    for j in prototipes:
        query = "SELECT * from celulares where id = " + str(j)
        arrDataBase[0].execute(query)
        resultados.append(arrDataBase[0].fetchall())
    arrDataBase[1].close()
    return resultados

def getAllDatabase():
    arrDataBase = openDatabase()
    query = ""
    resultados = []
    query = "SELECT * from celulares"
    arrDataBase[0].execute(query)
    resultados = arrDataBase[0].fetchall()
    arrDataBase[1].close()
    return resultados