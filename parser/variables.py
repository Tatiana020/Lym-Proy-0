import re

variables_globales = {}

def procesar_variables(linea):

    global variables_globales
    patron = r'^\|\s*([a-z][a-z0-9_]*(?:\s+[a-z][a-z0-9_]*)*)\s*\|$'
    match = re.match(patron, linea)

    if match:
        variables = match.group(1).split()
        for var in variables:
            variables_globales[var] = None 
        return True  
    return False 

def obtener_variables():

    return variables_globales
