import variables as v
condiciones_permitidas = ["facing","canPut","canPick","canMove","canJump","not"]
cardinales = ["#north", "#south", "#west", "#east"]
chips = [ "#ballons", "#chips"]
directions =["#north", "#south", "#west", "#east"]
funciones_permitidas = ["goTo","turn","face","put","pick","move","jump","nop", "if", "while", "for"]

def reconocer_codigo(linea):
    tokens = linea.split(" ")
    token = tokens[0]
    if token in funciones_permitidas:
        return reconocer_funcion(linea)
    if token in condiciones_permitidas:
        return reconocer_condicion(linea)
    else:
        return False
    
def reconocer_funcion(linea):
    tokens = linea.split(" ")
    token = tokens[0]
    if token == "goTo":
            resultado = leer_goto(linea)
    elif token == "turn":
            resultado = leer_turn(linea)
    elif token == "face":
            resultado = leer_face(linea)
    elif token == "put":
            resultado = leer_put(linea)
    elif token == "pick":
            resultado = leer_pick(linea)
    elif token == "move":
            resultado = leer_move(linea)
    elif token == "jump":
            resultado = leer_jump(linea)
    elif token == "nop":
            resultado = leer_nop(linea)
    return resultado

def reconocer_condicion(linea):
    tokens = linea.split(" ")
    token=tokens[0]
    resultado=True
    if token == "facing" or "canMove" or "canPut" or "canPick" or "canJump" or "not":
        resultado = leer_condicion(linea)
    elif token == "if":
        resultado = leer_condicional(linea)
    elif token == "while":
        resultado = leer_bucle(linea)
    elif token == "for":
        resultado = leer_repeticion(linea)
    return resultado
        
#Acciones
def leer_goto(linea):
    tokens = linea.split(" ")
    if len(tokens) == 5 and tokens[0] == "goTo:" and (tokens[1] in v.variables_globales or tokens[1].isdigit()) and tokens[2] == "with:" and (tokens[3] in v.variables_globales or tokens[3].isdigit()) and tokens[4] == ".":
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

def leer_move(linea):
    tokens = linea.split(" ")
    if len(tokens) == 5 and tokens[0] == "move:" and (tokens[1] in v.variables_globales or tokens[1].isdigit()) and tokens[2] == "toThe:" and tokens[3] in directions and tokens[4] == ".":
        return True
    if len(tokens) == 5 and tokens[0] == "move:" and (tokens[1] in v.variables_globales or tokens[1].isdigit()) and tokens[2] == "inDir:" and tokens[3] in cardinales and tokens[4] == ".":
        return True
    if len(tokens) == 3 and tokens[0] == "move:" and (tokens[1] in v.variables_globales or tokens[1].isdigit()) and tokens[2] == ".":
        return True
    return False

def leer_jump(linea):
    tokens = linea.split(" ")
    if len(tokens) == 5 and tokens[0] == "jump:" and (tokens[1] in v.variables_globales or tokens[1].isdigit()) and tokens[2] == "toThe:" and tokens[3] in directions and tokens[4] == ".":
        return True
    if len(tokens) == 5 and tokens[0] == "jump:" and (tokens[1] in v.variables_globales or tokens[1].isdigit()) and tokens[2] == "inDir:" and tokens[3] in cardinales and tokens[4] == ".":
        return True
    return False

def leer_nop(linea):
    tokens = linea.split(" ")
    if len(tokens) == 2 and tokens[0] == "nop" and tokens[1] == ".":
        return True
    return False

#Condiciones
# Función para leer un condicional
def leer_condicional(linea):
    if linea.startswith("if:"):
        partes = linea.split("then:")
        if len(partes) == 2:
            condicion = partes[0].strip()
            bloques = partes[1].split("else:")
            if len(bloques) == 2:
                bloque1 = bloques[0].strip()
                bloque2 = bloques[1].strip()
                if bloque1.startswith("[") and bloque1.endswith(" .]") and bloque2.startswith("[") and bloque2.endswith(" .]"):
                    return True
    return False

# Función para leer un bucle
def leer_bucle(linea):
    if linea.startswith("while:"):
        partes = linea.split("do:")
        if len(partes) == 2:
            condicion = partes[0].strip()
            bloque = partes[1].strip()
            if bloque.startswith("[") and bloque.endswith(" .]"):
                return True
    return False

# Función para leer una repetición
def leer_repeticion(linea):
    if linea.startswith("for:"):
        partes = linea.split("repeat:")
        if len(partes) == 2:
            contador = partes[0].strip()
            bloque = partes[1].strip()
            if bloque.startswith("[") and bloque.endswith(" .]"):
                return True
    return False

# Función para leer condiciones
def leer_condicion(linea):
    tokens = linea.split(" ")
    if len(tokens) == 3 and tokens[0] in ["facing:", "canMove:"] and tokens[2] == ".":
        if tokens[0] == "facing:" and tokens[1] in cardinales:
            return True
        if tokens[0] == "canMove:" and tokens[1].isdigit():
            return True
    elif len(tokens) == 5 and tokens[0] in ["canPut:", "canPick:", "canMove:", "canJump:"] and tokens[2] == "ofType:" and tokens[4] == ".":
        if tokens[0] in ["canPut:", "canPick:"] and tokens[3] in chips:
            return True
        if tokens[0] in ["canMove:", "canJump:"] and tokens[3] in cardinales:
            return True
    elif len(tokens) == 5 and tokens[0] in ["canMove:", "canJump:"] and tokens[2] == "toThe:" and tokens[4] == ".":
        if tokens[3] in directions:
            return True
    elif len(tokens) == 3 and tokens[0] == "not:":
        return leer_condicion(" ".join(tokens[1:]))
    return False
