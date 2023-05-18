from flask import Flask
from flask import render_template
from flask import request
from markupsafe import escape

from process import es_cadena_aritmetica_valida as validate

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def calcular():
    if request.method == 'POST':
        resultado = request.form.get('dato')
        if not validate(resultado):
            return render_template('calculadora.html')
        else:
            return render_template('calculadora.html', resultado=resultado)
        
    else:
        return render_template('calculadora.html')
    
    

# @app.route("/")
# def calculadora():
#     return render_template("calculadora.html")


@app.route("/hello")
def nom():
    return "saludo"

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

