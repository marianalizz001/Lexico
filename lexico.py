import sys
from enum import Enum

# Aqui van los tipos de Token
class TipoToken(Enum):
    # PALABRAS RESERVADAS main, if, then, else, end, do, while, cin, cout, real, int, boolean
    TKN_MAIN = 1  # MAIN
    TKN_IF = 2  # IF
    TKN_THEN = 3  # THEN
    TKN_ELSE = 4  # ELSE
    TKN_END = 5  # END
    TKN_DO = 6  # DO
    TKN_WHILE = 7  # WHILE
    TKN_CIN = 8  # CIN
    TKN_COUT = 9  # COUT
    TKN_REAL = 10  # REAL
    TKN_INT = 11  # INT
    TKN_BOOLEAN = 12  # BOOLEAN
    # Simbolos usados + - * /  % < <= > >= == != := ( ) { } // /**/ ++ --
    TKN_SUMA = 13  #'+'
    TKN_RESTA = 14  #'-'
    TKN_MULTIPLICACION = 15  #'*'
    TKN_DIVISION = 16  #'/'
    TKN_MODULO = 17  #'%'
    TKN_MENOR = 18  #'<'
    TKN_MENORIGUAL = 19  #'<='
    TKN_MAYOR = 20  #'>'
    TKN_MAYORIGUAL = 21  #'>='
    TKN_COMPARACION = 22  #'=='
    TKN_DIFERENTE = 23  #'!='
    TKN_ASIGNACION = 24  #':='
    TKN_LPARENTESIS = 25  #'('
    TKN_RPARENTESIS = 26  #')'
    TKN_LLAVEL = 27  #'{'
    TKN_LLAVER = 28  #'}'
    TKN_COMENLINEA = 29  #'//'
    TKN_COMENMULTLINEA = 30  #'/**/'
    TKN_INCREMENTO = 31  #'++'
    TKN_DECREMENTO = 32  #'--'
    # Otros
    TKN_IDENTIFICADOR = 33  # variable
    TKN_NUMERO = 34  # numero
    TKN_ERROR = 35  # error
    TKN_EOF = 36  # fin archivo


# Aqui van los estados
class Estados(Enum):
    IN_MAS = 1
    IN_MENOS = 2
    IN_MUL = 3
    IN_DIV = 4
    IN_MOD = 5
    IN_MENOR = 6
    IN_MENIG = 7
    IN_MAYOR = 8
    IN_MAYIG = 9
    IN_IGUALIGUAL = 10
    IN_DIF = 11
    IN_IGUAL = 12
    IN_PARENABRE = 13
    IN_PARENCIERRA = 14
    IN_LLAVEABRE = 15
    IN_LLAVECIERRA = 16
    IN_ID = 17
    IN_START = 18
    IN_ERROR = 19
    IN_DONE = 20
    IN_NUM = 21
    IN_NUM_FLOAT = 22
    IN_INCREMENTO = 23
    IN_DECREMENTO = 24
    IN_EOF = 25
    IN_COMENTARIOLINEA = 26
    IN_COMENTARIOMULTI = 27


# ABRIR ARCHIVO DE TEST
file = open("prueba.txt", "r")
cadena = file.read()
file.close()

index = 0
token = ""
tokens = []


def Numero():
    global token
    global index
    print "funcion numero"
    while cadena[index].isdigit() and index < len(cadena):
        print "si entro al while"
        print index
        token += cadena[index]
        print token
        index += 1
        print index
    print token

    # tokens.append(TipoToken.TKN_NUMERO)


while index < len(cadena):
    print len(cadena)
    if cadena[index].isdigit():
        print "si es un numero"
        Numero()

    index += 1


MAXTOKENLEN = 40
tokenString[MAXTOKENLEN + 1] = ""

# Funcion que va a tomar un nuevo caracter de el documento
def NuevoCaracter():
    hola = "hola"


# Funcion que va a ver que tipo de token es:
def getToken():
    tokenStringIndex = 0
    currentToken = TipoToken()
    state = Estados.IN_START
    save = 0
    while state != Estados.IN_DONE:
        c = NuevoCaracter()
        save = True
        if state == Estados.IN_START:
            if c.isdigit():
                state = Estados.IN_NUM
            elif c.isalpha():
                state = Estados.IN_ID


"""
def NuevoToken():
    print("Token = " + token + "\n")
    if (
        token in reservadas
    ):  # Si el token esta dentro de las palabras reservadas se identifica como tal
        tipoToken = "Palabra reservada"
    tokenInfo = [tInd, token, tipoToken]
    tokens.append(tokenInfo)
    tipoToken = ""
    token = ""


while cInd in range(len(cadena)):
    # TOKENS NUMERICOS
    if cadena[cInd] in numeros:
        Numeros()
    # TOKENS DE COMENTARIOS Y DIVISION
    elif cadena[cInd] == "/":
        Comentario()
    # TOKEN PARA IDENTIFICADOR
    elif cadena[cInd] in letras:
        Identificador()
    # SUMA Y... DOBLE SUMA jeje, RESTA Y... DOBLE RESTA jeje, MULTIPLICACION, RESIDUO, MENOR/MENOR IGUAL, MAYOR/MAYOR IGUAL, IGUALDAD Y ASIGNACION
    elif (
        cadena[cInd] == "+"
        or cadena[cInd] == "-"
        or cadena[cInd] == "*"
        or cadena[cInd] == "%"
        or cadena[cInd] == "<"
        or cadena[cInd] == ">"
        or cadena[cInd] == "="
    ):
        Operador()
    # PARENTESIS; CORCHETES Y LLAVES
    elif cadena[cInd] == "(":
        Coleccion()
    # ESPACIOS VACIOS
    elif cadena[cInd] == " ":
        cInd += 1
    # SALTOS DE LINEA
    elif "\n" in cadena[cInd]:
        SaltoLinea()
    # Identifica si se encontro algun token y lo ingresa en el arreglo#
    if len(token) != 0 and tipoToken != "":  # Nuevo token
        NuevoToken()
    if len(error) != 0 and tipoError != "":  # Nuevo error
        print("Entra un nuevo error:" + token + "\n")
        errorInfo = [tInd, error, tipoError]
        errores.append(errorInfo)
        tipoError = ""
        error = ""

"""
