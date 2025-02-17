import variables as v
procedimientos_definidos = {}

procedimientos_permitidos = ["goNorth", "goWest", "putChips", "turnLeft","turnRight",
                             "turnAround", "faceNorth","FaceSouth","FaceWest","FaceEast","putChips",
                             "putBallons","pickBallons","pickChips", "moveFront","moveBack","moveRight",
                             "moveLeft","moveO","jumpFront","jumpBack","jumpRight","jumpLeft","jumpO", "nop"]

condiciones_permitidas = ["facing","canPut","canPick","canMove","canJump","not"]
cardinales = ["#north", "#south", "#west", "#east"]
chips = [ "#ballons", "#chips"]
directions =["#north", "#south", "#west", "#east"]

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

    if nombre_proc not in procedimientos_permitidos:
        print(f"Error: El procedimiento '{nombre_proc}' no está permitido según el enunciado.")
        return False

    # Guardar 
    procedimientos_definidos[nombre_proc] = parametros
    print(f"Procedimiento registrado: {nombre_proc} con parámetros {parametros}")

    return True 


def leer_goto(linea):
    tokens = linea.split(" ")
    if len(tokens) == 5 and tokens[0] == "goTo:" and (tokens[1] in v.variables_globales or tokens[1].isdigit()) and tokens[2] == "with:" and (tokens[3] in v.variables_globales or tokens[3].isdigit()) and tokens[4] == ".":
        return True
    return False

def leer_move(linea):
    tokens = linea.split(" ")
    if len(tokens) == 3 and tokens[0] == "move:" and (tokens[1] in v.variables_globales or tokens[1].isdigit()) and tokens[2] == ".":
        return True
    return False

def leer_turn(linea):
    tokens = linea.split(" ")
    if len(tokens) == 3 and tokens[0] == "turn:" and tokens[1] in ["#left", "#right", "#around"] and tokens[2] == ".":
        return True
    return False

def leer_face(linea):
    tokens = linea.split(" ")
    if len(tokens) == 3 and tokens[0] == "face:" and tokens[1] in cardinales and tokens[2] == ".":
        return True
    return False

def leer_put(linea):
    tokens = linea.split(" ")
    if len(tokens) == 5 and tokens[0] == "put:" and (tokens[1] in v.variables_globales or tokens[1].isdigit()) and tokens[2] == "ofType:" and tokens[3] in chips and tokens[4] == ".":
        return True
    return False

def leer_pick(linea):
    tokens = linea.split(" ")
    if len(tokens) == 5 and tokens[0] == "pick:" and (tokens[1] in v.variables_globales or tokens[1].isdigit()) and tokens[2] == "ofType:" and tokens[3] in chips and tokens[4] == ".":
        return True
    return False

def leer_move_direction(linea):
    tokens = linea.split(" ")
    if len(tokens) == 5 and tokens[0] == "move:" and (tokens[1] in v.variables_globales or tokens[1].isdigit()) and tokens[2] == "toThe:" and tokens[3] in directions and tokens[4] == ".":
        return True
    return False

def leer_move_in_dir(linea):
    tokens = linea.split(" ")
    if len(tokens) == 5 and tokens[0] == "move:" and (tokens[1] in v.variables_globales or tokens[1].isdigit()) and tokens[2] == "inDir:" and tokens[3] in cardinales and tokens[4] == ".":
        return True
    return False

def leer_jump_direction(linea):
    tokens = linea.split(" ")
    if len(tokens) == 5 and tokens[0] == "jump:" and (tokens[1] in v.variables_globales or tokens[1].isdigit()) and tokens[2] == "toThe:" and tokens[3] in directions and tokens[4] == ".":
        return True
    return False

def leer_jump_in_dir(linea):
    tokens = linea.split(" ")
    if len(tokens) == 5 and tokens[0] == "jump:" and (tokens[1] in v.variables_globales or tokens[1].isdigit()) and tokens[2] == "inDir:" and tokens[3] in cardinales and tokens[4] == ".":
        return True
    return False

def leer_nop(linea):
    tokens = linea.split(" ")
    if len(tokens) == 2 and tokens[0] == "nop" and tokens[1] == ".":
        return True
    return False

def obtener_procedimientos():
    
    return procedimientos_definidos
