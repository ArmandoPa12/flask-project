import re

def es_cadena_aritmetica_valida(cadena ):

    operadores = ['+', '-', '*', '/']
    numeros = '0123456789'

    if len(cadena)== 0:
        return False

    # Verificar si la cadena contiene solo caracteres válidos
    for caracter in cadena:
        if caracter not in operadores and caracter not in numeros and caracter != ' ':
            return False

    # Verificar si hay operadores consecutivos
    for i in range(len(cadena) - 1):
        if cadena[i] in operadores and cadena[i + 1] in operadores:
            return False

    # Verificar si hay un operador al principio o al final de la cadena
    if cadena[0] in operadores or cadena[-1] in operadores:
        return False

    # Evaluar la cadena para verificar si es una expresión aritmética válida
    try:
        eval(cadena)
        return True
    except (SyntaxError, ZeroDivisionError):
        return False
    