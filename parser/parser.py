import variables as variables
import procedimientos as procedimientos
import codigo

def leer_archivo(ruta):
    resultado = True;
    ruta= "parser/" + ruta
    try:
        with open(ruta, 'r') as archivo:
            for_para_recursion(archivo)    
    except FileNotFoundError:
        print(f"El archivo en la {ruta} no se encontró")
    except Exception as e:
        print(f"Un error ocurrió: {e}")

def for_para_recursion(archivo):
    resultado = True
    for linea in archivo:
        tokens = linea.split(" ")
        for token in tokens:
            if token == "|":
                leer_variables(linea)
            elif token == "proc":
                leer_proc(linea)
            elif token == "[":
                leer_codigo(linea)
            else:
                leer_asignacion(linea)
    
def leer_variables(linea):
    if variables.procesar_variables(linea):
        print(f"Variables registradas: {list(variables.obtener_variables().keys())}")
        return True
    else:
        print(f"Error en declaración de variables: {linea}")
        return False

def leer_proc(archivo):
    return procedimientos.procesar_procedimiento(archivo, detallado=True)

def leer_asignacion(linea):
    resultado = True
    tokens = linea.split(" ")
    if tokens.lenght > 4:
        resultado = False
    if tokens [-1] != ".":
        resultado = False
    if tokens[-2] not in variables or (not int(tokens[-2])):
        resultado = False  
    if tokens [3,4] != ":=":
        resultado = False
    return resultado

def leer_codigo(linea):
    codigo.reconocer_codigo(linea)

leer_archivo("ejemploPrueba.txt")
