from antlr4 import*
from ExprLexer import ExprLexer
import sys

#LEER DESDE TERMINAL
#texto = input("Ingresa una expresion: ")
#input_stream = InputStream(texto)

#LEER ARCHIVOS
input_stream = FileStream(sys.argv[1])

# POR TERMINAL
lexer = ExprLexer(input_stream)

tokens = CommonTokenStream(lexer)
tokens.fill()
print(tokens)

for token in tokens.tokens:
    print("Texto: " + token.text)
    print("Linea:" + str(token.line))
    print("Columna:" + str(token.column))
    nombre_token = lexer.symbolicNames[token.type]
    print("Tipo: " + nombre_token)
    print("---------------------")