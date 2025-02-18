import variables as v
from parser import for_para_recursion 

procedimientos_definidos = {}

def procesar_procedimiento(archivo):

    global procedimientos_definidos

    lineas_procedimiento = []
    dentro_del_procedimiento = False
    corchetes_abiertos = 0
    encabezado = None

    for linea in archivo:
        linea = linea.strip()

        if linea.startswith("proc"):
            dentro_del_procedimiento = True
            encabezado = linea  # Guardar la primera linea
            continue

        if dentro_del_procedimiento:
            lineas_procedimiento.append(linea)

            corchetes_abiertos += linea.count("[")
            corchetes_abiertos -= linea.count("]")

        # Si ya cerramos todos los corchetes, termina de leer 
        if dentro_del_procedimiento and corchetes_abiertos == 0:
            dentro_del_procedimiento = False  

            if not encabezado or ":" not in encabezado:
                print("Falta ':' en la definición del procedimiento")
                return False

            nombre_proc, parametros = encabezado.replace("proc", "").strip().split(":", 1)
            nombre_proc = nombre_proc.strip()
            parametros = parametros.strip().split()


            if not nombre_proc.isidentifier():
                print("Error: Nombre de procedimiento inválido")
                return False

            # Guardamos
            procedimientos_definidos[nombre_proc] = {"parametros": parametros, "cuerpo": lineas_procedimiento}
            print(f"Procedimiento registrado: {nombre_proc} con parámetros {parametros}")

            # Procesar el contenido con la recursiva
            for linea_codigo in lineas_procedimiento:
                for_para_recursion([linea_codigo])  # Pasamos cada línea al parser

            # Reiniciamos 
            lineas_procedimiento = []
            corchetes_abiertos = 0

    return True  

def obtener_procedimientos():

    return procedimientos_definidos
