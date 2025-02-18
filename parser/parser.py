import variables as variables
import procedimientos as procedimientos

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
            elif token == "[]":
                        resultado = leer_codigo(linea)
            else:
                resultado = False
    
def leer_variables(linea):
    if variables.procesar_variables(linea):
        print(f"Variables registradas: {list(variables.obtener_variables().keys())}")
        return True
    else:
        print(f"Error en declaración de variables: {linea}")
        return False

def leer_proc(linea):

    reultado = procedimientos.procesar_procedimiento(linea)
    
    if resultado:
        print(f"Procedimiento registrado: {list(procedimientos.obtener_procedimientos().keys())}")
        return True 
    else:
        print(f"Error en declaración de procedimiento")
        return False 


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
    return True

def es_alfabetico(caracter):
    return caracter.isalpha()

def es_numerico(caracter):
    return caracter.isdigit()

leer_archivo("ejemploPrueba.txt")
