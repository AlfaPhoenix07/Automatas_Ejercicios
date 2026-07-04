from antlr4 import *
from ExprLexer import ExprLexer
import sys

# ==========================================
# OPCIÓN 1: LEER DESDE TERMINAL
# (Descomenta estas dos líneas y comenta la Opción 2)
# ==========================================
#texto = input("Ingresa una expresion: ")
#input_stream = InputStream(texto)


# ==========================================
# OPCIÓN 2: LEER DESDE ARCHIVO (sys.argv)
# (Descomenta esta línea y comenta la Opción 1)
# ==========================================
input_stream = FileStream(sys.argv[1], encoding='utf-8')


# ==========================================
# CÓDIGO PRINCIPAL (Este no se modifica)
# ==========================================
lexer = ExprLexer(input_stream)

tokens = CommonTokenStream(lexer)
tokens.fill()
print(tokens)

for token in tokens.tokens:
    # Omitimos el token EOF (Fin de archivo)
    if token.type == Token.EOF:
        continue
        
    print("Texto: " + token.text)
    print("Linea:" + str(token.line))
    print("Columna:" + str(token.column))
    
    # Aquí ya está corregido, llamando directamente a 'lexer'
    nombre_token = lexer.symbolicNames[token.type]
    
    print("Tipo: " + nombre_token)
    print("---------------------")