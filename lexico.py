import sys
from enum import Enum

# ABRIR ARCHIVO DE TEST
file = open("prueba.txt", "r")
cadena = file.read()
file.close()

# CREAR ARCHIVO DE TOKENS
f_token = open("tokens.txt", "w")
f_error = open("errores.txt", "w")


index = 0
token = ""


def EscribirToken(tipoToken, token):
    f_token.write("LexToken(" + tipoToken + "," + token + ")\n")


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
    print(index)
    print(len(cadena))
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
            EscribirToken("INCREMENTO", token)
            index += 1
        else:
            EscribirToken("MAS", token)
    print(token)


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
