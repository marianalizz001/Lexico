import sys

reservadas = [
    "main",
    "if",
    "then",
    "else",
    "end",
    "do",
    "while",
    "cin",
    "cout",
    "real",
    "int",
    "boolean",
]

# ABRIR ARCHIVO DE TEST

file = open(sys.argv[1], "r")
cadena = file.read()
file.close()

# CREAR ARCHIVO DE TOKENS
f_token = open(
    #"C:\\Users\\maria\\Desktop\\CompiLexico\\IdeCompilador\\src\\idecompilador\\tokens.txt","w",
    "/Users/KarenMarquez/NetBeansProjects/IdeCompilador/src/idecompilador/tokens.txt","w", 
)

# CREAR ARCHIVO DE ERRORES
f_error = open(
    #"C:\\Users\\maria\\Desktop\\CompiLexico\\IdeCompilador\\src\\idecompilador\\errores.txt","w",
    "/Users/KarenMarquez/NetBeansProjects/IdeCompilador/src/idecompilador/errores.txt", "w",
)

index = 0
linea = 1
columna = 1
token = ""


def EscribirToken(tipoToken, token, linea, columna):
    f_token.write("LexToken [ " + tipoToken + " , " + token + " , lin. " + str(linea) + " , col. " + str(columna)+ " ]\n")

def EscribirError(tipoError, token, linea, columna):
    f_error.write("LexError [ " + tipoError + " , " + token + " , lin. " + str(linea) + " , col. " + str(columna)+ " ]\n")

def Anterior():
    global index
    if index < (len(cadena) - 1):
        index -= 1

def Verificar(token_id):
    global columna
    global linea

    if token_id in reservadas:
        EscribirToken("PALABRA RESERVADA", token_id, linea, columna)
    else:
        EscribirToken("IDENTIFICADOR", token, linea, columna)


def Otro():
    global token
    global index
    global columna
    global linea
    token = ""
    token += cadena[index]
    EscribirError("Caracter invalido", token, linea, columna)
    index += 1
    columna -= 1

def Numero():
    global token
    global index
    global columna
    global linea
    token = ""
    salir = False
    flotante = False
    cont_puntos = 0
    band = 0
    while cadena[index].isdigit() and salir == False:
        columna += 1
        if index < (len(cadena) - 1):
            token += cadena[index]
            index += 1
        else:
            token += cadena[index]
            salir = True
    if cadena[index] == "." and cont_puntos == 0:
        columna += 1
        flotante = True
        salir = False
        token += cadena[index]
        index += 1
        cont_puntos += 1
        if not cadena[index].isdigit():
            salir = True
            EscribirError("Se esperaba un numero", token, linea, columna)
            band = 1
        while cadena[index].isdigit() and salir == False:
            columna += 1
            if index < (len(cadena) - 1):
                token += cadena[index]
                index += 1
            else:
                token += cadena[index]
                salir = True

    if band == 0:
        if (flotante == True):
            EscribirToken("NUMERO FLOTANTE", token, linea, columna)
        else:
            EscribirToken("NUMERO", token, linea, columna)


def Identificador():
    global token
    global index
    global columna
    global linea
    salir = False
    token = ""
    band = 0
    while (
        cadena[index].isalpha() or cadena[index].isdigit() or cadena[index] == "_"
    ) and salir == False:
        if index < (len(cadena) - 1) or cadena[index] != " " or cadena[index] != "\n":
            token += cadena[index]
            index += 1
            columna += 1
        else:
            token += cadena[index]
            salir = True
    Verificar(token)


def Operador():
    global token
    global index
    global columna
    global linea
    token = " "
    if cadena[index] == "+":
        token += cadena[index]
        index += 1
        columna += 1
        if cadena[index] == "+":
            token += cadena[index]
            EscribirToken("INCREMENTO", token, linea, columna)
            index += 1
            columna += 1
        else:
            EscribirToken("MAS", token, linea, columna)
    token = " "
    if cadena[index] == "-":
        token += cadena[index]
        index += 1
        columna += 1
        if cadena[index] == "-":
            token += cadena[index]
            EscribirToken("DECREMENTO", token, linea, columna)
            index += 1
            columna += 1
        else:
            EscribirToken("MENOS", token, linea, columna)
    token = " "
    if cadena[index] == "*":
        token += cadena[index]
        index += 1
        columna += 1
        if cadena[index] == "/":
            token += cadena[index]
            #EscribirToken("FIN COMENTARIO", token)
            index += 1
            columna += 1
        else:
            EscribirToken("MULTIPLICACION", token, linea, columna)
    token = " "
    if cadena[index] == "/":
        token += cadena[index]
        index += 1
        columna += 1
        hecho = 0
        if cadena[index] == "/":
            token += cadena[index]
            #EscribirToken("COMENTARIO SENCILLO", token)
            while cadena[index] != "\n":
                index += 1
                columna += 1
        elif cadena[index] == "*":
            token += cadena[index]
            #EscribirToken("INICIO COMENTARIO", token)
            while hecho == 0:
                index += 1
                columna += 1
                if cadena[index] == "*":
                    token = ""
                    token += cadena[index]
                    index += 1
                    columna += 1
                    if cadena[index] == "/":
                        token += cadena[index]
                        #EscribirToken("FIN COMENTARIO", token)
                        index += 1
                        columna += 1
                        hecho = 1
        else:
            EscribirToken("DIVISION", token, linea, columna)
    token = " "
    if cadena[index] == "%":
        token += cadena[index]
        index += 1
        columna += 1
        EscribirToken("RESIDUO", token, linea, columna)


def Menor():
    global token
    global index
    global columna
    global linea
    token = " "
    if cadena[index] == "<":
        token += cadena[index]
        index += 1
        columna += 1
        if cadena[index] == "=":
            token += cadena[index]
            EscribirToken("MENOR IGUAL", token, linea, columna)
            index += 1
            columna += 1
        else:
            EscribirToken("MENOR", token, linea, columna)


def Mayor():
    global token
    global index
    global columna
    global linea
    token = " "
    if cadena[index] == ">":
        token += cadena[index]
        index += 1
        columna += 1
        if cadena[index] == "=":
            token += cadena[index]
            EscribirToken("MAYOR IGUAL", token, linea, columna)
            index += 1
            columna += 1
        else:
            EscribirToken("MAYOR", token, linea, columna)


def Igualdad():
    global token
    global index
    global columna
    global linea
    token = " "
    if cadena[index] == "=":
        token += cadena[index]
        index += 1
        columna += 1
        if cadena[index] == "=":
            token += cadena[index]
            EscribirToken("COMPARADOR", token, linea, columna)
            index += 1
            columna += 1
        else:
            EscribirError("Se esperaba un =", token, linea, columna)


def Diferente():
    global token
    global index
    global columna
    global linea
    token = " "
    if cadena[index] == "!":
        token += cadena[index]
        index += 1
        columna += 1
        if cadena[index] == "=":
            token += cadena[index]
            EscribirToken("DIFERENTE", token, linea, columna)
            index += 1
            columna += 1
        else:
            EscribirError("Se esperaba un =", token, linea, columna)


def Asignacion():
    global token
    global index
    global columna
    global linea
    token = " "
    if cadena[index] == ":":
        token += cadena[index]
        index += 1
        columna += 1
        if cadena[index] == "=":
            token += cadena[index]
            EscribirToken("ASIGNACION", token, linea, columna)
            index += 1
            columna += 1
        else:
            EscribirError("Se esperaba un =", token, linea, columna)


def Parentesis():
    global token
    global index
    global columna
    global linea
    token = " "
    if cadena[index] == "(":
        token += cadena[index]
        EscribirToken("PARENTESIS IZQ", token, linea, columna)
    elif cadena[index] == ")":
        token += cadena[index]
        EscribirToken("PARENTESIS DER", token, linea, columna)
    index += 1
    columna += 1


def Llaves():
    global token
    global index
    global columna
    global linea
    token = " "
    if cadena[index] == "{":
        token += cadena[index]
        EscribirToken("LLAVE IZQ", token, linea, columna)
    elif cadena[index] == "}":
        token += cadena[index]
        EscribirToken("LLAVE DER", token, linea, columna)
    index += 1
    columna += 1

def Puntos():
    global token
    global index
    global columna
    global linea
    token = " "
    if cadena[index] == ".":
        token += cadena[index]
        EscribirToken("PUNTO", token, linea, columna)
    if cadena[index] == ",":
        token += cadena[index]
        EscribirToken("COMA", token, linea, columna)
    if cadena[index] == ";":
        token += cadena[index]
        EscribirToken("PUNTOYCOMA", token, linea, columna)
    index += 1
    columna += 1

while index < len(cadena):
    entrar = 0
    if cadena[index] == "\n":
        linea += 1
        columna = 1
    entrar = 0
    if cadena[index].isdigit():
        Numero()
        Anterior()
        entrar = 1
    elif cadena[index].isalpha():
        Identificador()
        Anterior()
        entrar = 1
    elif (
        cadena[index] == "+"
        or cadena[index] == "-"
        or cadena[index] == "*"
        or cadena[index] == "/"
        or cadena[index] == "%"
    ):
        Operador()
        Anterior()
        entrar = 1
    elif cadena[index] == "<":
        Menor()
        Anterior()
        entrar = 1
    elif cadena[index] == ">":
        Mayor()
        Anterior()
        entrar = 1
    elif cadena[index] == "=":
        Igualdad()
        Anterior()
        entrar = 1
    elif cadena[index] == "!":
        Diferente()
        Anterior()
        entrar = 1
    elif cadena[index] == ":":
        Asignacion()
        Anterior()
        entrar = 1
    elif cadena[index] == "(" or cadena[index] == ")":
        Parentesis()
        Anterior()
        entrar = 1
    elif cadena[index] == "{" or cadena[index] == "}":
        Llaves()
        Anterior()
        entrar = 1
    elif cadena[index] == "." or cadena[index] == "," or cadena[index] == ";":
        Puntos()
        Anterior()
        entrar = 1
    if entrar == 0 and cadena[index] != " " and cadena[index] != "\n":
        Otro()
        Anterior()

    index += 1

f_token.close()
f_error.close()
