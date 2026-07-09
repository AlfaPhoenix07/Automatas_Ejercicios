from antlr4 import *
from ExprLexer import ExprLexer;
from ExprParser import ExprParser

entrada = input("Codigo:")
lexer = ExprLexer(InputStream(entrada))
tokens = CommonTokenStream(lexer)
parser = ExprParser(tokens)
arbol = parser.root()
#print("arbol: ")
#print(arbol.toStringTree(recog=parser))

if parser.getNumberOfSyntaxErrors() == 0:
    print("El codigo es correcto")
    print("Arbol: ")
    print(arbol.toStringTree(recog=parser))
else:   
    print("El codigo tiene errores de sintaxis")
