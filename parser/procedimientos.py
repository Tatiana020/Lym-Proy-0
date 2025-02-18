import variables as v

procedimientos_definidos = {}

def procesar_procedimiento(archivo, detallado=False):

    global procedimientos_definidos
    from parser import for_para_recursion  

    lineas_procedimiento = []
    dentro_del_procedimiento = False
    corchetes_abiertos = 0
    encabezado = None
    nombre_proc = None  

    for linea in archivo:
        linea = linea.strip()

        if linea.startswith("proc"):
            dentro_del_procedimiento = True
            encabezado = linea  
            if detallado:
                print(f"Encabezado detectado -> '{encabezado}'")  
            continue  

        if dentro_del_procedimiento:
            if linea != "":  
                lineas_procedimiento.append(linea)
                corchetes_abiertos += linea.count("[")
                corchetes_abiertos -= linea.count("]")

        if dentro_del_procedimiento and corchetes_abiertos == 0:
            dentro_del_procedimiento = False  

            if detallado:
                print(f"Encabezado antes de procesar -> '{encabezado}'")

            encabezado = encabezado.replace("proc", "", 1).strip()
            if ":" in encabezado:
                nombre_proc, parametros = encabezado.split(":", 1)
                nombre_proc = nombre_proc.strip()
                parametros = parametros.strip().split()
            else:
                if detallado:
                    print(f"Procedimiento sin parámetros detectado -> '{encabezado}'")
                nombre_proc = encabezado.replace("[", "").strip()
                parametros = []  

            if not nombre_proc.isidentifier():
                if detallado:
                    print(f"Error: Nombre de procedimiento inválido '{nombre_proc}'")
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

    return True  

def obtener_procedimientos():
    return procedimientos_definidos


def obtener_procedimientos():
    return procedimientos_definidos
