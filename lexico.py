from enum import Enum
class Reservadas(Enum):
    #PALABRAS RESERVADAS main, if, then, else, end, do, while, cin, cout, real, int, boolean
	TKN_MAIN = 1		    #MAIN
	TKN_IF = 2				#IF
	TKN_THEN = 3			#THEN
	TKN_ELSE = 4			#ELSE
	TKN_END = 5				#END
	TKN_DO = 6	    		#DO
	TKN_WHILE = 7			#WHILE
	TKN_CIN = 8			    #CIN
	TKN_COUT = 9		    #COUT
	TKN_REAL = 10			#REAL
	TKN_INT = 11			#INT
	TKN_BOOLEAN = 12		#BOOLEAN

class Simbolos(Enum):
	#Simbolos usados + - * /  % < <= > >= == != := ( ) { } // /**/ ++ -- 
	TKN_SUMA = 1			#'+'
	TKN_RESTA = 2			#'-'
	TKN_MULTIPLICACION = 3	#'*'
	TKN_DIVISION = 4		#'/'
	TKN_MODULO = 5			#'%'
	TKN_MENOR = 6			#'<'
	TKN_MENORIGUAL = 7		#'<='
	TKN_MAYOR = 8			#'>'
	TKN_MAYORIGUAL = 9		#'>='
	TKN_COMPARACION	= 10	#'=='
	TKN_DIFERENTE = 11		#'!='
	TKN_ASIGNACION = 12		#':='
	TKN_LPARENTESIS	= 13	#'('
	TKN_RPARENTESIS	= 14	#')'
	TKN_LLAVEL = 15			#'{'
	TKN_LLAVER = 16			#'}'
	TKN_COMENLINEA = 17     #'//'
	TKN_COMENMULTLINEA = 18 #'/**/'
	TKN_INCREMENTO = 19 	#'++'
	TKN_DECREMENTO = 20 	#'--'

class Otros(Enum):	
	TKN_IDENTIFICADOR = 1	#variable
	TKN_NUMERO = 2		    #numero
	TKN_ERROR = 3			#error
	TKN_EOF = 4				#fin archivo

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
	IN_DECREMENTO =24
	IN_EOF = 25
	IN_COMENTARIOLINEA = 26
	IN_COMENTARIOMULTI = 27
class Token(object):
	
		
