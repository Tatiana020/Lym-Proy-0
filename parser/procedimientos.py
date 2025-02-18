import variables as v

procedimientos_definidos = {}

def procesar_procedimiento(archivo, detallado=False):

    global procedimientos_definidos
    from parser import for_para_recursion  

    lineas_procedimiento = []
    dentro_del_procedimiento = False
    corchetes_abiertos = 0
    nombre_proc = None  

    for linea in archivo:
        linea = linea.strip()

        if linea.startswith("proc"):
            dentro_del_procedimiento = True
            encabezado = linea.replace("proc", "", 1).strip()
            continue  
        
        if not dentro_del_procedimiento:
            print(f"Error: Se encontró código fuera de un procedimiento -> '{linea}'")
            return False

        if dentro_del_procedimiento:
            if linea != "":  
                lineas_procedimiento.append(linea)
                corchetes_abiertos += linea.count("[")
                corchetes_abiertos -= linea.count("]")

        if dentro_del_procedimiento and corchetes_abiertos == 0:
            dentro_del_procedimiento = False  

            if not encabezado or "[" not in encabezado:
                print(f"Error: Procedimiento mal definido, falta '[' -> '{encabezado}'")
                return False

            if ":" in encabezado:
                nombre_proc, parametros = encabezado.split(":", 1)
                nombre_proc = nombre_proc.strip()
                parametros = parametros.strip().split()
            else:
                nombre_proc = encabezado.replace("[", "").strip()
                parametros = []  

            if not nombre_proc.isidentifier():
                print(f"Error: Nombre de procedimiento inválido -> '{nombre_proc}'")
                return False

            if corchetes_abiertos != 0:
                print(f"Error: Corchetes desbalanceados en procedimiento -> '{nombre_proc}'")
                return False

            procedimientos_definidos[nombre_proc] = {
                "parametros": parametros,
                "cuerpo": lineas_procedimiento
            }

            if detallado:
                print(f"Procedimiento registrado: {nombre_proc} con parámetros {parametros}")
                print(f"Contenido del procedimiento: {lineas_procedimiento}")

            for linea_codigo in lineas_procedimiento:
                for_para_recursion([linea_codigo])  

            lineas_procedimiento = []
            corchetes_abiertos = 0

    print("Todos los procedimientos procesados correctamente.")
    return True  

def obtener_procedimientos():
    return procedimientos_definidos
