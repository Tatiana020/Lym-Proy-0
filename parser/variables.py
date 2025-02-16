variables_globales = {}

def procesar_variables(linea):
    global variables_globales

    if not (linea.startswith("|") and linea.endswith("|")):
        print("La declaración de variables debe estar entre | ... |")
        return False

    contenido = linea[1:-1].strip()

    variables = contenido.split()

    for var in variables:
        if not var[0].isalpha():
            print(f"La variable '{var}' no empieza con una letra")
            return False
        if not var.isalnum() and "_" not in var:  # Solo letras, números y '_'
            print(f"La variable '{var}' contiene caracteres no permitidos")
            return False

    for var in variables:
        variables_globales[var] = None 

    print(f"Variables registradas: {list(variables_globales.keys())}")
    return True  

def obtener_variables():

    return variables_globales
