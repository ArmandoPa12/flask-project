from flask import Flask
from flask import render_template
from flask import request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route('/calcular', methods=['POST'])
def calcular():
    numero1 = float(request.form['numero1'])
    numero2 = float(request.form['numero2'])
    operacion = request.form['operacion']

    resultado = None

    if operacion == 'suma':
        resultado = numero1 + numero2
    elif operacion == 'resta':
        resultado = numero1 - numero2
    elif operacion == 'multiplicacion':
        resultado = numero1 * numero2
    elif operacion == 'division':
        resultado = numero1 / numero2

    return render_template('index.html', resultado=resultado)

@app.route("/calculadora")
def calculadora():
    return render_template("calculadora.html")


@app.route("/hello")
def nom():
    return "saludo"

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

