

def leer_archivo(ruta):
    resultado = True;
    try:
        with open(ruta, 'r') as archivo:
            for linea in archivo:
                print(linea.strip())
    except FileNotFoundError:
        print(f"TEl archivo en la {ruta} no se encontró")
    except Exception as e:
        print(f"Un error ocurrió: {e}")

def leer_variables(linea):
    return True

def leer_proc(linea):
    return True

def leer_codigo(linea):
    return True