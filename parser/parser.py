import variables as variables
import procedimientos as procedimientos
import codigo

def leer_archivo(ruta):
    resultado = True
    ruta = "parser/" + ruta
    try:
        with open(ruta, 'r') as archivo:
            contenido = archivo.read().strip()
            if not contenido:
                print(f"El archivo {ruta} está vacío")
                return False
            archivo.seek(0)  # Reset file pointer to the beginning
            return for_para_recursion(archivo)
    except FileNotFoundError:
        print(f"El archivo en la {ruta} no se encontró")
    except Exception as e:
        print(f"Un error ocurrió: {e}")

def for_para_recursion(archivo):
    resultado = True
    for linea in archivo:
        tokens = linea.split(" ")
        token = tokens[0]
        if token == "|":
            resultado = leer_variables(linea)
        elif token == "proc":
            resultado = leer_proc(archivo)
        elif token == "[":
            resultado = leer_codigo(linea)
        elif ":=" in tokens:
            resultado=leer_asignacion(linea)
        elif codigo.reconocer_codigo(linea):
            resultado = leer_codigo(linea)
        else:
            resultado = False
    return resultado

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
    linea = linea.strip()

    if not linea.endswith("."):
        return False

    linea = linea[:-1].strip()

    tokens = linea.split(" ")

    if len(tokens) != 3:
        return False
    
    variable, operador, valor = tokens

    if operador != ":=":
        return False
    
    if not variable.isidentifier():
        return False

    if not valor.isdigit():
        return False

    return True

def leer_codigo(linea):
    codigo.reconocer_codigo(linea)

print(leer_archivo("ejemplo.txt"))
