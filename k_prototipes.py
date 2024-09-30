import math

from databaseController import getAllDatabase

def controller_Kprototipes(prototipes,numberPrototipes):
     iter = 0
     _continue = True
     discriminate_protoripes = numberPrototipes
     new_prototipes_old_list = []
     new_prototipes = []
     total_result = []
     parsial_result = {}
     #se hace la primer iteracion

     new_prototipes_list = k_prototipes(prototipes, discriminate_protoripes)
     total_result.append({
          'prototipes' : prototipes, 
          'collection' : new_prototipes_list
          })

     # se genera un auxiliar en cada iteracion, para poder comparar el que viene y el anterior
     while _continue :
          if(iter == 0):
               iter += 1
               new_prototipes_old_list = new_prototipes_list
               new_prototipes = generate_new_prototipes(new_prototipes_list)
               new_prototipes_list = k_prototipes(new_prototipes,discriminate_protoripes)
               total_result.append({
                    'prototipes' : new_prototipes, 
                    'collection' : new_prototipes_list
                    })
               
          else:
               iter += 1
               if(iter < 5000):
                    if(check_if_iterate(new_prototipes_old_list,new_prototipes_list)):
                         new_prototipes_old_list = new_prototipes_list
                         new_prototipes = generate_new_prototipes(new_prototipes_list)
                         
                         new_prototipes_list = k_prototipes(new_prototipes, discriminate_protoripes)  
                         total_result.append({
                              'prototipes' : new_prototipes, 
                              'collection' : new_prototipes_list
                              })
                         
                    else:
                         _continue = False
               else:
                    _continue = False
                    total_result = [{'status' : "error"}]

          
     return total_result

def k_prototipes(prototipes, discriminate_protoripes):
     # generando un diccionario tomando en cuenta el numero de k's elegidos
     iterations_results = {}
     collections_prototipes = {}
     for i in range(len(prototipes)):
          collections_prototipes[f'k{i}'] = []
          
          
     for register in getAllDatabase(discriminate_protoripes):
        
          for i in range(len(prototipes)):
               iterations_results[f'k{i}'] = '0'
               
          for indice_prototipes, prototipe in enumerate(prototipes):

               sumatoria_cuadrado = 0
               sumatoria_categoricos = 0
               iterations_results[f'k{indice_prototipes}'] = '0'

               for indice_prototipe, elemento in enumerate(prototipe):
                    
                    if isinstance(elemento, (int, float)):
               
                         resta = register[indice_prototipe] - elemento
                         cuadrado = pow(resta, 2)
                         sumatoria_cuadrado += cuadrado
                    else:
                         
                         if(register[indice_prototipe].strip().lower() != elemento.strip().lower() ):
                              sumatoria_categoricos += 1

               sumatoria_cuadrado = math.sqrt(sumatoria_cuadrado)

               iterations_results[f"k{indice_prototipes}"] = sumatoria_cuadrado + sumatoria_categoricos
                  
               if( indice_prototipes + 1 == len(prototipes)):
                   
                    min_key = min(iterations_results, key=iterations_results.get)
                   
                    collections_prototipes[f'{min_key}'].append(register)

     return collections_prototipes

               
def check_if_iterate(old, current):
     
     for clave, valor in old.items():
          old[clave].sort()
          current[clave].sort()
          
     if(old == current):
         
          return False
     else:
          
          return True
     
def generate_new_prototipes(list_k):


     list_numbers = []
     list_words = []
     result_list = []
     isNumber = True
     buildTupla = ()
     listTuplas = {}
     count_words = {}
     # inicializando la listTuplas con las k's, si k =4, entonces se va a inicializar de k0 a k3
     for k in list_k:
          listTuplas[k] = []
     for k in list_k:
          # validando si la kn tiene alguin elemento, si esta vacia, entonces no se ejecuta
          if(len(list_k[k]) > 0):
               # sacando la primer tupla de las k's e iterando las posiciones de esta tupla
               for position in range(len(list_k[k][0])):
                    # la avriable data contiene toda la info de cada k, si tiene 3 tuplas, entonces data las contiene
                    for data in list_k[k]:
                         # verificando si la posicion de la tupla es un numero (numerico)
                         if isinstance(data[position], (int, float)):
                              # como es numerico se agrega a una lista de numeros, en este caso de la k que se esta iterando
                              list_numbers.append(data[position])
                              # marcamos la bandera que es numero
                              isNumber = True
                         else:
                              # como no es numerico, entonces es categorico, se agrega a una lista de categoricos, en este caso de la k que se esta iterando
                              list_words.append(data[position])
                              # marcamos la bandera que no es numero
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
                    

               