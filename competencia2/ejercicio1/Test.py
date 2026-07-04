from antlr4 import *
from ExprLexer import ExprLexer
import sys

# LEER ARCHIVOS usando el argumento pasado en la terminal
input_stream = FileStream(sys.argv[1], encoding='utf-8')

lexer = ExprLexer(input_stream)

tokens = CommonTokenStream(lexer)
tokens.fill()
print(tokens)

for token in tokens.tokens:
    # Es buena práctica ignorar el token EOF (Fin de archivo) para limpiar la salida
    if token.type == Token.EOF:
        continue
        
    print("Texto: " + token.text)
    print("Linea:" + str(token.line))
    print("Columna:" + str(token.column))
    
    # CORRECCIÓN: Usamos la variable 'lexer' directamente
    nombre_token = lexer.symbolicNames[token.type]
    
    print("Tipo: " + nombre_token)
    print("---------------------")