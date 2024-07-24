import math

from databaseController import getAllDatabase

def controller_Kprototipes(prototipes):
     new_prototipes = k_prototipes(prototipes)
     
          # comparar los diccionarios

               # si prototipes es igual a  new_prototipes entonces 
               
                    # finaliza la ejecucion y sacamos resultado a usuario

               # si prototipes no es igual a  new_prototipes entonces 
               
                    # generamos n iteraciones hasta que new (n) _prototipes se aigual a new (n + 1) _prototipes
          
    # new_prototipes_2 = k_prototipes(new_prototipes)

def k_prototipes(prototipes):
     # generando un diccionario tomando en cuenta el numero de k's elegidos
     iterations_results = {}
     collections_prototipes = {}
     for i in range(len(prototipes)):
          iterations_results[f'k{i}'] = '0'
          collections_prototipes[f'k{i}'] = '0'
          
          
     for register in getAllDatabase():

          # distancia datos mezclados
          for indice_prototipes, prototipe in enumerate(prototipes):
               sumatoria_cuadrado = 0
               sumatoria_categoricos = 0
               
               ##print(f"{indice_prototipes}, {prototipe}")
               
               # tenemos una base de datos con datos categoricos y numericos
               
               #      tomando un registro, vamos a ir verificando que el dato que estemos comparando sea un int o string
                    
               #      de acuerdo a el resultado utilizamos el metodo de 
               #print("++++++++++++++inicio++++++++++++++++++++")
               #print(f"se revisa el prototipo k{indice_prototipes} con valores {prototipe[0]}")
               #print(f"se revisa el registro con valores {register}")

               for indice_prototipe, elemento in enumerate(prototipe[0]):
                    ##print(f"indice {indice_prototipe} , elemento: {elemento}")
                    if isinstance(elemento, (int, float)):
               #           datos numericos

               #                si se va a este metodo entonces lo regresamos como cuadrado
                              
               #                se genera este paso cuantas veces sea necesaria
                              
               #                al final se suman todos y se saca la raiz
                              
               #                seguimos la ejecucion de revision
                         #print(f"es numerico")
                         #print(f"se hace la resta {register[indice_prototipe]} - {elemento}")
                         resta = register[indice_prototipe] - elemento
                         cuadrado = pow(resta, 2)
                         #print(f"resultado resta = {resta}")
                         #print(f"resultado cuadrado = {cuadrado}")
                         #print(f"sumatoria cuadrado = {sumatoria_cuadrado}")

                         sumatoria_cuadrado += cuadrado
                    else:
                         #print(f"es categorico")
                         #print(f"se compara {register[indice_prototipe]}  ==  {elemento}")
                         ##print(f"el indice {indice_prototipe} es string y es {register[indice_prototipe]}")
                         if(register[indice_prototipe].strip().lower() != elemento.strip().lower() ):
                              sumatoria_categoricos += 1
                         
                         
               
                         
               #           datos categoricos

               #                     verifivamos si son iguales, si si 
                                   
               #                          es igual a 0
               #                     si no
                                   
               #                          es 1
               #                el resultado se regresa 
                              
               #                se hace la suma total
               #      sacamos raiz cuadrada de la suma delos numericos
               sumatoria_cuadrado = math.sqrt(sumatoria_cuadrado)
               #print(f"Sumatoria cuadrado final = {sumatoria_cuadrado}")

               #      se suma el resultado de los datos numericos y categoricos
                         
               #      el resultado se guarda en el indice correspondiente
               iterations_results[f"k{indice_prototipes}"] = sumatoria_cuadrado + sumatoria_categoricos
               
               print(iterations_results)
               for i in range(len(prototipes)):
                    iterations_results[f'k{i}'] = '0'
                    #collections_prototipes[f'k{i}'] = '0'
               #print("+++++++++++++fin+++++++++++++++++++++")
                    
               #      comparamos todos los indices y el indice mas pequeño gana

               #           este objeto n se guarda en un diccionario collections_prototipes
                         
               #           para finalizar se obtiene la moda y el promedio por cada collection y se queda una sola posicion 