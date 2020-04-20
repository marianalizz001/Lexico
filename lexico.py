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

# CREAR ARCHIVO DE TOKENS
f_token = open("tokens.txt", "wb")
f_error = open("errores.txt", "wb")


index = 0
token = ""


def EscribirToken(tipoToken, token):
    f_token.write("LexToken(" + str(tipoToken) + "," + str(token) + ")\n")


def Anterior():
    global index
    if index < (len(cadena) - 1):
        index -= 1


def Numero():
    global token
    global index
    token = ""
    salir = False
    while cadena[index].isdigit() and salir == False:
        if index < (len(cadena) - 1):
            token += cadena[index]
            index += 1
        else:
            token += cadena[index]
            salir = True
    print(token)
    EscribirToken("NUMERO", token)
    # tokens.append(TipoToken.TKN_NUMERO)


def Identificador():
    global token
    global index
    salir = False
    token = ""
    while cadena[index].isalpha() and salir == False:
        if index < (len(cadena) - 1):
            token += cadena[index]
            index += 1
        else:
            token += cadena[index]
            salir = True
    EscribirToken("IDENTIFICADOR", token)
    print(token)


def Mas():
    global token
    global index
    salir = False
    token = " "
    if cadena[index] == "+":
        token += cadena[index]
        index += 1
        if cadena[index] == "+":
            token += cadena[index]
    print(token)
    EscribirToken("MAS", token)


while index < len(cadena):
    if cadena[index].isdigit():
        print("Es un numero")
        Numero()
        Anterior()
    elif cadena[index].isalpha():
        print("Es una letra")
        Identificador()
        Anterior()
    elif cadena[index] == "+":
        print("Es un mas")
        Mas()
        Anterior()
    index += 1
print("Se acabo")

f_token.close()
f_error.close()
