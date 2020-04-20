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
	f_token.write("LexToken[ " + tipoToken + "," + token + " ]\n")


def EscribirError(tipoError, token):
	f_error.write("Error[ " + tipoError + "," + token + " ]\n")


def Anterior():
	global index
	if index < (len(cadena) - 1):
		index -= 1


def Verificar(token_id):
	if token_id in reservadas:
		EscribirToken("PALABRA RESERVADA", token_id)
	else:
		EscribirToken("IDENTIFICADOR", token)


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
	band = 0
	while (
		cadena[index].isalpha() or cadena[index].isdigit() or cadena[index] == "_"
	) and salir == False:
		if index < (len(cadena) - 1) or cadena[index] != " " or cadena[index] != "\n":
			token += cadena[index]
			index += 1
		else:
			token += cadena[index]
			salir = True
	if (
		cadena[index] != "_"
		and (not cadena[index].isdigit())
		and (not cadena[index].isalpha())
		and cadena[index] != " "
		and cadena[index] != "\n"
	):
		EscribirError("No es un valor esperado", cadena[index])
	Verificar(token)


def Operador():
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

	if cadena[index] == "-":
		token += cadena[index]
		index += 1
		if cadena[index] == "-":
			token += cadena[index]
			EscribirToken("DECREMENTO", token)
			index += 1
		else:
			EscribirToken("MENOS", token)

	if cadena[index] == "*":
		token += cadena[index]
		index += 1
		if cadena[index] == "/":
			token += cadena[index]
			EscribirToken("FIN COMENTARIO", token)
			index += 1
		else:
			EscribirToken("MULTIPLICACION", token)

	if cadena[index] == "/":
		token += cadena[index]
		index += 1
		hecho = 0
		if cadena[index] == "/":
			token += cadena[index]
			EscribirToken("COMENTARIO SENCILLO", token)
			while cadena[index] != "\n":
				index += 1
		elif cadena[index] == "*":
			token += cadena[index]
			EscribirToken("INICIO COMENTARIO", token)
			while hecho == 0:
				index += 1
				if cadena[index] == "*":
					token = ""
					token += cadena[index]
					index += 1
					if cadena[index] == "/":
						token += cadena[index]
						EscribirToken("FIN COMENTARIO", token)
						index += 1
						hecho = 1
		else:
			EscribirToken("DIVISION", token)

	if cadena[index] == "%":
		token += cadena[index]
		index += 1
		EscribirToken("RESIDUO", token)


def Menor():
	global token
	global index
	token = " "
	if cadena[index] == "<":
		token += cadena[index]
		index += 1
		if cadena[index] == "=":
			token += cadena[index]
			EscribirToken("MENOR IGUAL", token)
			index += 1
		else:
			EscribirToken("MENOR", token)


def Mayor():
	global token
	global index
	token = " "
	if cadena[index] == ">":
		token += cadena[index]
		index += 1
		if cadena[index] == "=":
			token += cadena[index]
			EscribirToken("MAYOR IGUAL", token)
			index += 1
		else:
			EscribirToken("MAYOR", token)


def Igualdad():
	global token
	global index
	token = " "
	if cadena[index] == "=":
		token += cadena[index]
		index += 1
		if cadena[index] == "=":
			token += cadena[index]
			EscribirToken("IGUALDAD", token)
			index += 1
		else:
			EscribirError("Se esperaba otro =", token)


def Diferente():
	global token
	global index
	token = " "
	if cadena[index] == "!":
		token += cadena[index]
		index += 1
		if cadena[index] == "=":
			token += cadena[index]
			EscribirToken("DIFERENTE", token)
			index += 1
		else:
			EscribirError("Se esperaba un =", token)


def Asignacion():
	global token
	global index
	token = " "
	if cadena[index] == ":":
		token += cadena[index]
		index += 1
		if cadena[index] == "=":
			token += cadena[index]
			EscribirToken("ASIGNACION", token)
			index += 1
		else:
			EscribirError("Se esperaba un =", token)


def Parentesis():
	global token
	global index
	token = " "
	if cadena[index] == "(":
		token += cadena[index]
		EscribirToken("PARENTESIS IZQ", token)
	elif cadena[index] == ")":
		token += cadena[index]
		EscribirToken("PARENTESIS DER", token)
	index += 1


def Llaves():
	global token
	global index
	token = " "
	if cadena[index] == "{":
		token += cadena[index]
		EscribirToken("LLAVE IZQ", token)
	elif cadena[index] == "}":
		token += cadena[index]
		EscribirToken("LLAVE DER", token)
	index += 1


while index < len(cadena):
	if cadena[index].isdigit():
		Numero()
		Anterior()
	elif cadena[index].isalpha():
		Identificador()
		Anterior()
	elif (
		cadena[index] == "+"
		or cadena[index] == "-"
		or cadena[index] == "*"
		or cadena[index] == "/"
		or cadena[index] == "%"
	):
		Operador()
		Anterior()
	elif cadena[index] == "<":
		Menor()
		Anterior()
	elif cadena[index] == ">":
		Mayor()
		Anterior()
	elif cadena[index] == "=":
		Igualdad()
		Anterior()
	elif cadena[index] == "!":
		Diferente()
		Anterior()
	elif cadena[index] == ":":
		Asignacion()
		Anterior()
	elif cadena[index] == "(" or cadena[index] == ")":
		Parentesis()
		Anterior()
	elif cadena[index] == "{" or cadena[index] == "}":
		Llaves()
		Anterior()

	index += 1

f_token.close()
f_error.close()
