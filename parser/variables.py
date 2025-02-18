variables_globales = {}

def procesar_variables(linea, detallado=False):

    global variables_globales

    print(f"Analizando línea de variables: '{linea}'")  

    if not (linea.startswith("|") and linea.endswith("|")):
        if detallado:
            print("Error: La declaración de variables debe estar entre | ... |")
        return False

    contenido = linea[1:-1].strip()  
    variables = contenido.split()

    if not variables:
        print("Error: No se encontraron variables dentro de '| ... |'")
        return False

    for var in variables:
        print(f"Verificando variable: {var}") 
        if not var[0].isalpha():
            print(f"Error: La variable '{var}' no empieza con una letra")
            return False
        if not var.isalnum() and "_" not in var: 
            print(f"Error: La variable '{var}' contiene caracteres no permitidos")
            return False

    for var in variables:
        variables_globales[var] = None 

    print(f"Variables registradas correctamente: {list(variables_globales.keys())}")

    return True  

def obtener_variables():
    """
    Devuelve el diccionario de variables registradas.
    """
    return variables_globales
