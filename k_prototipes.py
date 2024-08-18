import math

from databaseController import getAllDatabase
#controlador que manda a llamar todo 
#controlador si se tiene que volver a iterar o no
def controller_Kprototipes(prototipes):
     iter = 0
     _continue = True
     new_prototipes_old_list = []
     new_prototipes = []
     #se hace la primer iteracion
     print("*****************")
     print(f'nuevos prototipos : {new_prototipes}')
     print("")
     new_prototipes_list = k_prototipes(prototipes)
     print(f'la lista vieja es : {new_prototipes_old_list}')  
     print("") 
     print(f'la lista nueva es : {new_prototipes_list}')   
     print("*****************")
     # se genera un auxiliar en cada iteracion, para poder comparar el que viene y el anterior
     while _continue :
          if(iter == 0):
               iter += 1
               #print("se debe de repetir")
               new_prototipes_old_list = new_prototipes_list
               new_prototipes = generate_new_prototipes(new_prototipes_list)
               print("*****************")
               print(f'nuevos prototipos : {new_prototipes}')
               print("")
               new_prototipes_list = k_prototipes(new_prototipes)
               print(f'la lista vieja es : {new_prototipes_old_list}')  
               print("") 
               print(f'la lista nueva es : {new_prototipes_list}')   
               print("*****************")
          else:
               if(check_if_iterate(new_prototipes_old_list,new_prototipes_list)):
                    new_prototipes_old_list = new_prototipes_list
                    new_prototipes = generate_new_prototipes(new_prototipes_list)
                    print("*****************")
                    print(f'nuevos prototipos : {new_prototipes}')
                    print("")
                    new_prototipes_list = k_prototipes(new_prototipes)  
                    print(f'la lista vieja es : {new_prototipes_old_list}')  
                    print("") 
                    print(f'la lista nueva es : {new_prototipes_list}')   
                    print("*****************")


               else:
                    #print("no se debe de repetir")
                    _continue = False


          # comparar los diccionarios

               # si prototipes es igual a  new_prototipes_list entonces 
               
                    # finaliza la ejecucion y sacamos resultado a usuario

               # si prototipes no es igual a  new_prototipes_list entonces 
               
                    # generamos n iteraciones hasta que new (n) _prototipes se aigual a new (n + 1) _prototipes
          
    # new_prototipes_2 = k_prototipes(new_prototipes_list)

def k_prototipes(prototipes):
     # generando un diccionario tomando en cuenta el numero de k's elegidos
     iterations_results = {}
     collections_prototipes = {}
     for i in range(len(prototipes)):
          collections_prototipes[f'k{i}'] = []
          
          
     for register in getAllDatabase():
          ##print("++++++++++++++inicio++++++++++++++++++++")
          for i in range(len(prototipes)):
               iterations_results[f'k{i}'] = '0'
               
          for indice_prototipes, prototipe in enumerate(prototipes):

               sumatoria_cuadrado = 0
               sumatoria_categoricos = 0
               iterations_results[f'k{indice_prototipes}'] = '0'
               #collections_prototipes[f'k{indice_prototipes}'] = ''
               
               ###print(f"{indice_prototipes}, {prototipe}")
               
               # tenemos una base de datos con datos categoricos y numericos
               
               #      tomando un registro, vamos a ir verificando que el dato que estemos comparando sea un int o string
                    
               #      de acuerdo a el resultado utilizamos el metodo de 
               # ##print(f"se revisa el prototipo k{indice_prototipes} con valores {prototipe[0]}")
               # ##print(f"se revisa el registro con valores {register}")

               for indice_prototipe, elemento in enumerate(prototipe):
                    ####print(f"indice {indice_prototipe} , elemento: {elemento}")
                    if isinstance(elemento, (int, float)):
               #           datos numericos

               #                si se va a este metodo entonces lo regresamos como cuadrado
                              
               #                se genera este paso cuantas veces sea necesaria
                              
               #                al final se suman todos y se saca la raiz
                              
               #                seguimos la ejecucion de revision
                         ###print(f"es numerico")
                         ###print(f"se hace la resta {register[indice_prototipe]} - {elemento}")
                         resta = register[indice_prototipe] - elemento
                         cuadrado = pow(resta, 2)
                         ###print(f"resultado resta = {resta}")
                         ###print(f"resultado cuadrado = {cuadrado}")
                         ###print(f"sumatoria cuadrado = {sumatoria_cuadrado}")

                         sumatoria_cuadrado += cuadrado
                    else:
                         ###print(f"es categorico")
                         ###print(f"se compara {register[indice_prototipe]}  ==  {elemento}")
                         ####print(f"el indice {indice_prototipe} es string y es {register[indice_prototipe]}")
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
               ###print(f"Sumatoria cuadrado final = {sumatoria_cuadrado}")

               #      se suma el resultado de los datos numericos y categoricos
                         
               #      el resultado se guarda en el indice correspondiente
               iterations_results[f"k{indice_prototipes}"] = sumatoria_cuadrado + sumatoria_categoricos
                  
               ###print(iterations_results)
  
         
               if( indice_prototipes + 1 == len(prototipes)):
                    ##print(iterations_results)
                    min_key = min(iterations_results, key=iterations_results.get)
                    ##print(f'el valor mas chico es {min_key}')
                    collections_prototipes[f'{min_key}'].append(register)

     return collections_prototipes
               # for i in range(len(prototipes)):
               #      iterations_results[f'k{i}'] = '0'
               #      #collections_prototipes[f'k{i}'] = '0'
                    
               ###print("+++++++++++++fin+++++++++++++++++++++")
                    
               #      comparamos todos los indices y el indice mas pequeño gana

               #           este objeto n se guarda en un diccionario collections_prototipes
                         
               #           para finalizar se obtiene la moda y el promedio por cada collection y se queda una sola posicion 
               
def check_if_iterate(old, current):
     ## ordenando las listas
     if(sorted(old) == sorted(current)):
          return False
     else:
          return True
     
def generate_new_prototipes(list_k):
     #print("**********")
     #print(list_k)
     #print("**********")

     list_numbers = []
     list_words = []
     result_list = []
     isNumber = True
     buildTupla = ()
     listTuplas = {}
     count_words = {}
     for k in list_k:
          listTuplas[k] = []
     for k in list_k:
          if(len(list_k[k]) > 0):
               for position in range(len(list_k[k][0])):
                    for data in list_k[k]:
                         if isinstance(data[position], (int, float)):
                              list_numbers.append(data[position])
                              isNumber = True
                         else:
                              list_words.append(data[position])
                              isNumber = False
                              
                    if(isNumber):       
                         suma_total = sum(list_numbers)
                         cantidad_elementos = len(list_numbers)
                         promedio = suma_total / cantidad_elementos
                         buildTupla += (promedio,)
                         list_numbers = []
                    else:
                         for words in list_words:
                              if words in count_words:
                                   count_words[words] += 1
                              else:
                                   count_words[words] = 1
                         avg_word = max(count_words, key=count_words.get)
                         buildTupla += (avg_word,)
                         list_words = []
                         count_words = {}

          listTuplas[k].append(buildTupla)
          buildTupla = ()

     #refactorizando respuesta para iteraciones
     for new_k in listTuplas:
          result_list.append(listTuplas[new_k][0])
     
     return result_list
                    