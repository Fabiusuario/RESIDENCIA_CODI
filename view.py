from databaseController import *


def kprototipes_view (data):
    
    data_prototipes = data['data']
    collaps = ''
    desplagete_btns = ''
    desplagete_tables = ''
    build_rows_table = ''
    build_header_table = ''
    build_table_prototipe = ''
    
    for indice, valor in enumerate(data_prototipes):
        build_header_table = ''
        build_table_prototipe = ''
        # print(valor['prototipes'])
        # print(valor['collection'])
        
        ## construyenndo las colecicones
        for clave_col, valor_col in valor['collection'].items():
            desplagete_btns += f'''
                    <a class="btn btn-primary" data-toggle="collapse" href="#multiCollapse{clave_col}{indice}" role="button" aria-expanded="false" aria-controls="multiCollapse{clave_col}{indice}">Mostrar agrupamiento {clave_col}</a>
                    '''
        
        for header in getHeaderTable():
            build_header_table += f'<th scope="col">{header}</th>'
                    
        for clave_col, valor_col in valor['collection'].items():    
            build_rows_table = ''        
            for data_tupla in valor_col:
                build_rows_table += '<tr>'
                for single_value_tupa in data_tupla:
                    build_rows_table += f'''
                                <td>{single_value_tupa}</td>
                            '''
                build_rows_table += '</tr>'
                
            desplagete_tables += f'''
                    <div class="row">
                    <div class="col">
                        <div class="collapse multi-collapse" id="multiCollapse{clave_col}{indice}">
                        <div class="card card-body">
                            <p>Agrupacion {clave_col}</p>
                            <div class='table-responsive'>
                                <table class="table table-hover">
                                    <thead>
                                        <tr>
                                            {build_header_table}
                                        </tr>
                                    </thead>
                                    <tbody>
                                    {build_rows_table}
                                    </tbody>
                                </table>
                            </div>
                        </div>
                        </div>
                    </div>
                    </div>'''

        for tupla_final_prototipe in valor['prototipes']:
            build_table_prototipe += f'''<div class='table-responsive'><table class="table table-hover">
                                            <thead>
                                                <tr>
                                                    {build_header_table}
                                                </tr>
                                            </thead>
                                            <tbody>'''
            for value_tupla_prototipe in tupla_final_prototipe:
                build_table_prototipe += f'''<td>
                                                {value_tupla_prototipe}
                                            </td>'''
            build_table_prototipe += '''
                                    </tbody>
                                        </table></div>'''
                            
        collaps += f'''<div class="card">
                <div class="card-header" id="heading{indice}">
                <h5 class="mb-0">
                    <button class="btn btn-link" data-toggle="collapse" data-target="#collapse{indice}" aria-expanded="true" aria-controls="collapse{indice}">
                    Iteración #{indice}
                    </button>
                </h5>
                </div>

                <div id="collapse{indice}" class="collapse" aria-labelledby="heading{indice}" data-parent="#accordion">
                <div class="card-body">
                {build_table_prototipe}
                <hr>
                <p>
                {desplagete_btns}
                </p>
                <div class="row">
                {desplagete_tables}
                </div>
                </div>
                </div>
            </div>'''
        desplagete_btns = ''
        desplagete_tables = ''
    
    html = f'''
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Ejemplo de Bootstrap 4</title>
            <!-- Bootstrap CSS -->
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        </head>
        <body>

        <div class="container mt-5">
            <!-- Título -->
            <h1 class="text-center">K - PROTOTYPES  </h1>

            <!-- Input con Label -->
            <form action="/kprototipes" method="POST">
                <div class="row">
                    <div class="form-group col-12">
                        <label for="nombre">K centros iniciales :</label>
                        <input type="number" value = '{data['k_number']}' class="form-control" id="nombre" placeholder="2" disabled>
                    </div>
                </div>
            </form>
            <form action="/init" method="GET">
                <button class="btn btn-success" type="submit">Volver a calcular</button>
            </form>
            <div id="accordion">
            {collaps}
            </div>
        </div>

        <!-- Bootstrap JS y dependencias -->
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

        </body>
        </html>
        '''
    return html

def home ():
    html = '''
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Ejemplo de Bootstrap 4</title>
            <!-- Bootstrap CSS -->
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        </head>
        <body>
        <div class="container">
         <!-- Título -->
        <h1 class="text-center">K - PROTOTYPES  </h1>

        <!-- Input con Label -->
        <form action="/kprototipes" method="POST">
            <div class="row">
            <div class="col-12 form-group">
                <label for="k_number">K centros iniciales :</label>
                <input type="number" class="form-control" id="k_number" name="k_number" placeholder="Ejemplo : 2" required>
            </div>
            </div>
            <div class="row">
                <div class="col-12">
                    <button type="submit" class="btn btn-success">Enviar</button>
                </div>
            </div>
        </form>
        </div>

        <!-- Bootstrap JS y dependencias -->
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

        </body>
        </html>
        '''
    return html

def errorDatabase():
    html = '''<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
                 <!-- Bootstrap CSS -->
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
            </head>
           <body class='container'>
            <div class='row'>
                <div class="alert alert-warning mt-5" role="alert">
                    <h4 class="alert-heading">Aviso</h4>
                    <p>La base de datos es muy pequeña, para que el sistema funcione correctamente se necesita probar con un conjunto de datos mas grande o vuelva a intentar, ya que las combinaciones pueden ser diferentes</p>
                    <div class="row">
                        <div class="col-12">
                            <button type="button" class="btn btn-primary" onclick="goBack()">Regresar</button>
                        </div>
                    </div>
                </div>
            </div>
                <script>
                    function goBack() {
                        window.history.back();
                    }
                </script>
                <!-- Bootstrap JS y dependencias -->
                <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
                <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js"></script>
                <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
            </body>
            </html>'''
    return html