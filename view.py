

def kprototipes_view (data):
    
    data_prototipes = data['data']
    collaps = ''
    desplagete_btns = ''
    desplagete_tables = ''
    
    
    for indice, valor in enumerate(data_prototipes):
        print(valor['prototipes'])
        print(valor['collection'])
        
        ## construyenndo las colecicones
        for clave_col, valor_col in valor['collection'].items():
            desplagete_btns += f'''
                    <a class="btn btn-primary" data-toggle="collapse" href="#multiCollapse{clave_col}{indice}" role="button" aria-expanded="false" aria-controls="multiCollapse{clave_col}{indice}">Mostrar agrupamiento {clave_col}</a>
                    '''
        
        for clave_col, valor_col in valor['collection'].items():
            
            
            desplagete_tables += f'''
                    <div class="row">
                    <div class="col">
                        <div class="collapse multi-collapse" id="multiCollapse{clave_col}{indice}">
                        <div class="card card-body">
                            <p>Agrupacion {clave_col}</p>
                            
                        </div>
                        </div>
                    </div>
                    </div>'''

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
                Prototipos : {valor['prototipes']}
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
                <div class="form-group">
                    <label for="nombre">K centros iniciales :</label>
                    <input type="number" value = '{data['k_number']}' class="form-control" id="nombre" placeholder="2" disabled>
                </div>
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
                <input type="number" class="form-control" id="k_number" name="k_number" placeholder="2">
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