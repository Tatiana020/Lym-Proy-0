import variables as v
condiciones_permitidas = ["facing","canPut","canPick","canMove","canJump","not"]
cardinales = ["#north", "#south", "#west", "#east"]
chips = [ "#ballons", "#chips"]
directions =["#north", "#south", "#west", "#east"]
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
