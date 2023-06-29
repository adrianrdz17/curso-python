from flask import Flask, request, url_for, redirect, abort, render_template

app = Flask(__name__)

import mysql.connector

midb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="gustavo01",
    database="prueba"
)

# Convierto mi cursor en un diccionario, lo que me permite usar indices nombrados y no solo numericos
cursor = midb.cursor(dictionary=True)

# Para configurar el servidor, como servidor de desarrollo utilizamos los siguientes comandos
# export FLASK_DEBUG=1
# Esto para linux, ahora solo corremos la aplicacion


@app.route('/')
def index():
    return 'hola mundo'

# Variables en las rutas e incorporacion de metodos HTTP
@app.route('/post/<post_id>', methods=['GET', 'POST'])
def post(post_id):
    if request.method == 'GET':
        return 'El id del post es: ' + post_id
    else:
        return 'Este es otro metodo y no get'

# Comando con curl para formulario
# curl -X POST -F 'campo1=valor1' -F 'campo2=valor2' http://localhost:5000/form
@app.route('/form', methods = ['GET', 'POST'])
def form():
    cursor.execute('select * from Usuario')
    usuarios = cursor.fetchall()
    # print(usuarios)
    # Aqui se abortan peticiones
    # abort(404)
    # Aqui se indica el nombre de la funcion del endpoint y despues el valor de los argumentos para la funcion
    # Importante el return para que muestre el endpoint deseado
    # return redirect(url_for('post', post_id=2))

    # Aqui se renderizan plantillas (estas deben de estar dentro de un directorio llamado 'templates')
    # return(render_template('users.html'))

    # Aqui se responde con un JSON
    # return {
        # 'username': 'chanchito feliz',
        # 'email': 'chanchito@feliz.com'
    # }

    # print(request.form)
    # print(request.form['campo1'])

    return render_template('users.html', usuarios=usuarios)

# Aqui extendemos una plantilla mediante el envio de un mensaje a esta para despues renderizar dentro de ella
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', mensaje = 'Hola mundo')

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Obtengo datos del formulario
        username = request.form['username']
        email = request.form['email']
        edad = request.form['edad']

        # Creo la consulta SQL de Insercion
        sql = 'insert into Usuario (username, email, edad) values (%s, %s, %s)'
        values = (username, email, edad)
        cursor.execute(sql, values)
        midb.commit()
        return redirect(url_for('form'))
    else:
        return render_template('create.html')