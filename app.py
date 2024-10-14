from flask import Flask, request
from view import home, kprototipes_view, errorDatabase
from controllerK_prototipes import init_kprototipes
from pyngrok import ngrok

# Crear la instancia de Flask
app = Flask(__name__)

@app.route('/init', methods=['GET'])
def init():
    return home()

@app.route('/kprototipes', methods=['POST'])
def kprototipes():
    data = {}
    data['k_number'] = request.form['k_number']
    data['data'] = init_kprototipes(data['k_number'])

    if 'status' in data['data'][0]:
        return errorDatabase()
    else:
        return kprototipes_view(data)


# Configurar ngrok para conectarse al puerto 5000
public_url = ngrok.connect(5000)
print("ngrok tunnel URL:", public_url)

if __name__ == '__main__':
    app.run()

    
