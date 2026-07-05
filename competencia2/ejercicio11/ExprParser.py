# Generated from Expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,49,10,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,0,0,2,0,2,0,0,
        7,0,4,1,0,0,0,2,7,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,
        8,5,0,0,1,8,3,1,0,0,0,0
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'public'", "'class'", "'static'", "'void'", 
                     "'int'", "'double'", "'string'", "'boolean'", "'for'", 
                     "'while'", "'do'", "'get'", "'set'", "'new'", "'Scanner'", 
                     "'if'", "'else'", "'import'", "'private'", "'this'", 
                     "'null'", "'true'", "'false'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'='", "'=='", "'+'", "'-'", "'*'", "'%'", 
                     "'/'", "'>'", "'<'", "'>='", "'<='", "'++'", "'--'", 
                     "'('", "')'", "'{'", "'}'", "';'", "':'", "'.'", "'['", 
                     "']'" ]

    symbolicNames = [ "<INVALID>", "PUBLIC", "CLASS", "STATIC", "VOID", 
                      "INT", "DOUBLE", "STRING", "BOOLEAN", "FOR", "WHILE", 
                      "DO", "GET", "SET", "NEW", "SCANNER", "IF", "ELSE", 
                      "IMPORT", "PRIVATE", "THIS", "NULL", "TRUE", "FALSE", 
                      "ID", "NUM", "CADENA", "IGUAL", "IGUAL_IGUAL", "MAS", 
                      "MENOS", "MULTI", "MODULO", "DIVISION", "MAYOR", "MENOR", 
                      "MAYOR_IGUAL", "MENOR_IGUAL", "MAS_MAS", "MENOS_MENOS", 
                      "PAR_IZQ", "PAR_DER", "LLAVE_IZQ", "LLAVE_DER", "PUNTO_COMA", 
                      "DOS_PUNTOS", "PUNTO", "COR_IZQ", "COR_DER", "WS" ]

    RULE_root = 0
    RULE_expr = 1

    ruleNames =  [ "root", "expr" ]

    EOF = Token.EOF
    PUBLIC=1
    CLASS=2
    STATIC=3
    VOID=4
    INT=5
    DOUBLE=6
    STRING=7
    BOOLEAN=8
    FOR=9
    WHILE=10
    DO=11
    GET=12
    SET=13
    NEW=14
    SCANNER=15
    IF=16
    ELSE=17
    IMPORT=18
    PRIVATE=19
    THIS=20
    NULL=21
    TRUE=22
    FALSE=23
    ID=24
    NUM=25
    CADENA=26
    IGUAL=27
    IGUAL_IGUAL=28
    MAS=29
    MENOS=30
    MULTI=31
    MODULO=32
    DIVISION=33
    MAYOR=34
    MENOR=35
    MAYOR_IGUAL=36
    MENOR_IGUAL=37
    MAS_MAS=38
    MENOS_MENOS=39
    PAR_IZQ=40
    PAR_DER=41
    LLAVE_IZQ=42
    LLAVE_DER=43
    PUNTO_COMA=44
    DOS_PUNTOS=45
    PUNTO=46
    COR_IZQ=47
    COR_DER=48
    WS=49

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_root




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr()
            self.state = 5
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





