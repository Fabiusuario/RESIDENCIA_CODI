import sqlite3
import random
import pandas as pd
   
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
    query = "SELECT count(*) from categoria"
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
        query = "SELECT * from categoria where id = " + str(j)
        arrDataBase[0].execute(query)
        for i in arrDataBase[0].fetchall():
            resultados.append(i)
    arrDataBase[1].close()
    return resultados

def getAllDatabase():
    arrDataBase = openDatabase()
    query = ""
    resultados = []
    query = "SELECT * from categoria"
    arrDataBase[0].execute(query)
    resultados = arrDataBase[0].fetchall()
    arrDataBase[1].close()
    return resultados

def readCsv():
    arrDataBase = openDatabase()
    
    df = pd.read_csv('PoblacionEstudiantil2.csv')
    query = '''insert into poblacion (	
    id,
	edad,
	sexo,
	carrera,
	semestre,
	e_civil,
	salud_fisica,
	salud_psicologica,
	relaciones_sociales,
	entorno,
	interpretacion,
	cie1,
	cie2,
	cie3,
	cie4,
	cie5,
	cie6,
	cie11,
	cie12,
	cie13,
	cie16,
	cie17,
	cie18,
	cie19,
	cie20,
	cie21,
	cie22,
	d_ind,
	d_colec,
	baston,
	andadera,
	muletas,
	silla_de_ruedas,
	protesis,
	lentes,
	aparato_auditivo,
	ayuda_de_alguien,
	otro,
	min_transporte,
	computadora,
	laptop,
	smartphone,
	tablet,
	internet_fijo,
	impresora,
	vehiculo_propio,
	closest) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    for index, row in df.iterrows():
        arrDataBase[0].execute(query
        , (row.id,
            row.edad,
            row.sexo,
            row.carrera,
            row.semestre,
            row.e_civil,
            row.salud_fisica,
            row.salud_psicologica,
            row.relaciones_sociales,
            row.entorno,
            row.interpretacion,
            row.cie1,
            row.cie2,
            row.cie3,
            row.cie4,
            row.cie5,
            row.cie6,
            row.cie11,
            row.cie12,
            row.cie13,
            row.cie16,
            row.cie17,
            row.cie18,
            row.cie19,
            row.cie20,
            row.cie21,
            row.cie22,
            row.d_ind,
            row.d_colec,
            row.baston,
            row.andadera,
            row.muletas,
            row.silla_de_ruedas,
            row.protesis,
            row.lentes,
            row.aparato_auditivo,
            row.ayuda_de_alguien,
            row.otro,
            row.min_transporte,
            row.computadora,
            row.laptop,
            row.smartphone,
            row.tablet,
            row.internet_fijo,
            row.impresora,
            row.vehiculo_propio,
            row.closest))
        
        arrDataBase[1].commit()

