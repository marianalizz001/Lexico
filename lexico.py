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
file = open("prueba.txt", "r")
cadena = file.read()
file.close()

# CREAR ARCHIVO DE TOKENS
f_token = open("tokens.txt", "w")

# CREAR ARCHIVO DE ERRORES
f_error = open("errores.txt", "w")

index = 0
token = ""


def EscribirToken(tipoToken, token):
    f_token.write("LexToken(" + tipoToken + "," + token + ")\n")


def EscribirError(tipoError, token):
    f_error.write("Error(" + tipoError + "," + token + ")\n")


def Anterior():
    global index
    if index < (len(cadena) - 1):
        index -= 1


def Numero():
    global token
    global index
    token = ""
    salir = False
    cont_puntos = 0
    band = 0
    while cadena[index].isdigit() and salir == False:
        if index < (len(cadena) - 1):
            token += cadena[index]
            index += 1
        else:
            token += cadena[index]
            salir = True
    if cadena[index] == "." and cont_puntos == 0:
        salir = False
        token += cadena[index]
        index += 1
        cont_puntos += 1
        while cadena[index].isdigit() and salir == False:
            if index < (len(cadena) - 1):
                token += cadena[index]
                index += 1
            else:
                token += cadena[index]
                salir = True
        if not cadena[index].isdigit() and cadena[index] != "\n":
            EscribirError("Se esperaba un numero", token)
            salir = True
            band = 1
    if band == 0:
        EscribirToken("NUMERO", token)


def Identificador():
    global token
    global index
    salir = False
    token = ""
    while (
        cadena[index].isalpha() or cadena[index].isdigit() or cadena[index] == "_"
    ) and salir == False:
        if index < (len(cadena) - 1) or cadena[index] != " " or cadena != "\n":
            token += cadena[index]
            index += 1
        else:
            token += cadena[index]
            salir = True
    EscribirToken("IDENTIFICADOR", token)


def Mas():
    global token
    global index
    token = " "
    if cadena[index] == "+":
        token += cadena[index]
        index += 1
        if cadena[index] == "+":
            token += cadena[index]
            EscribirToken("INCREMENTO", token)
            index += 1
        else:
            EscribirToken("MAS", token)

def Menos():
    global token
    global index
    token = " "
    if cadena[index] == "-":
        token += cadena[index]
        index += 1
        if cadena[index] == "-":
            token += cadena[index]
            EscribirToken("DECREMENTO", token)
            index += 1
        else:
            EscribirToken("MENOS", token)

def Multiplicacion():
    global token
    global index
    token = " "
    if cadena[index] == "*":
        token += cadena[index]
        index += 1
        if cadena[index] == "/":
            token += cadena[index]
            EscribirToken("FIN COMENTARIO", token)
            index += 1
        else:
            EscribirToken("MULTIPLICACION", token)

def Division():
    global token
    global index
    token = " "
    if cadena[index] == "/":
        token += cadena[index]
        index += 1
        if cadena[index] == "/":
            token += cadena[index]
            EscribirToken("COMENTARIO SENCILLO", token)
            index += 1
        elif cadena[index] == "*":
            token += cadena[index]
            EscribirToken("INICIO COMENTARIO", token)
            index += 1
        else:
            EscribirToken("DIVISION", token)

def Residuo():
    global token
    global index
    token = " "
    if cadena[index] == "%":
        token += cadena[index]
        index += 1
        EscribirToken("RESIDUO", token)
          
while index < len(cadena):
    if cadena[index].isdigit():
        Numero()
        Anterior()
    elif cadena[index].isalpha():
        Identificador()
        Anterior()
    elif cadena[index] == "+":
        Mas()
        Anterior()
    elif cadena[index] == "-":
        Menos()
        Anterior()
    elif cadena[index] == "*":
        Multiplicacion()
        Anterior()
    elif cadena[index] == "/":
        Division()
        Anterior()
    elif cadena[index] == "%":
        Residuo()
        Anterior()
    index += 1

f_token.close()
f_error.close()
