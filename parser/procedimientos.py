import variables as v
procedimientos_definidos = {}


def procesar_procedimiento(linea):
    global procedimientos_definidos

    # Verificar que la linea empieza con proc y contiene "[  ]"
    if not (linea.startswith("proc") and "[" in linea and "]" in linea):
        print("La línea no es un procedimiento válido")
        return False

    partes = linea.split("[", 1)
    encabezado = partes[0].strip()  # Obtiene el inicio sin espacios extra


    if not linea.endswith("]"):
        print("Falta ']' en el procedimiento")
        return False

    if ":" not in encabezado:
        print("Falta ':' para separar el nombre del procedimiento y los parámetros")
        return False

    nombre_proc, parametros = encabezado.replace("proc", "").strip().split(":", 1)

    # Limpiar espacios 
    nombre_proc = nombre_proc.strip()
    parametros = parametros.strip().split() 

    # Verificar que el nombre del procedimiento es valido 
    if not nombre_proc.isidentifier():
        print(f"Nombre de procedimiento inválido '{nombre_proc}'")
        return False

    # Guardar 
    procedimientos_definidos[nombre_proc] = parametros
    print(f"Procedimiento registrado: {nombre_proc} con parámetros {parametros}")

    return True 


def obtener_procedimientos():
    
    return procedimientos_definidos
