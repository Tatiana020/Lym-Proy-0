import variables.py

def leer_archivo(ruta):
    resultado = True;
    ruta= "parser/" + ruta
    try:
        with open(ruta, 'r') as archivo:
            for linea in archivo:
                None
    except FileNotFoundError:
        print(f"El archivo en la {ruta} no se encontró")
    except Exception as e:
        print(f"Un error ocurrió: {e}")

def leer_variables(linea):
    if variables_manager.procesar_variables(linea):
        print(f"Variables registradas: {list(variables_manager.obtener_variables().keys())}")
        return True
    else:
        print(f"Error en declaración de variables: {linea}")
        return False

def leer_proc(linea):
    return True

def leer_codigo(linea):
    return True

def es_alfabetico(caracter):
    return caracter.isalpha()

def es_numerico(caracter):
    return caracter.isdigit()

leer_archivo("ejemploPrueba.txt")
