from flask import Flask, request

# Crear la instancia de Flask
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        return f"Welcome, {username}!"
    return '''
        <form method="post">
            <p><input type="text" name="username"></p>
            <p><input type="submit" value="Login"></p>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
