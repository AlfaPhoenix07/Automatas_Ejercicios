# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,47,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,0,1,1,4,1,20,8,1,11,1,12,1,21,1,1,5,1,25,8,1,10,
        1,12,1,28,9,1,1,2,4,2,31,8,2,11,2,12,2,32,1,3,1,3,1,4,1,4,1,5,1,
        5,1,6,4,6,42,8,6,11,6,12,6,43,1,6,1,6,0,0,7,1,1,3,2,5,3,7,4,9,5,
        11,6,13,7,1,0,4,2,0,65,90,97,122,3,0,48,57,65,90,97,122,1,0,48,57,
        3,0,9,10,13,13,32,32,50,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,
        1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,1,15,1,0,0,0,3,19,
        1,0,0,0,5,30,1,0,0,0,7,34,1,0,0,0,9,36,1,0,0,0,11,38,1,0,0,0,13,
        41,1,0,0,0,15,16,5,105,0,0,16,17,5,102,0,0,17,2,1,0,0,0,18,20,7,
        0,0,0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,
        26,1,0,0,0,23,25,7,1,0,0,24,23,1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,
        0,26,27,1,0,0,0,27,4,1,0,0,0,28,26,1,0,0,0,29,31,7,2,0,0,30,29,1,
        0,0,0,31,32,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,6,1,0,0,0,34,
        35,5,62,0,0,35,8,1,0,0,0,36,37,5,40,0,0,37,10,1,0,0,0,38,39,5,41,
        0,0,39,12,1,0,0,0,40,42,7,3,0,0,41,40,1,0,0,0,42,43,1,0,0,0,43,41,
        1,0,0,0,43,44,1,0,0,0,44,45,1,0,0,0,45,46,6,6,0,0,46,14,1,0,0,0,
        5,0,21,26,32,43,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ID = 2
    NUM = 3
    MAYOR_QUE = 4
    PAR_IZQ = 5
    PAR_DER = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'>'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ID", "NUM", "MAYOR_QUE", "PAR_IZQ", "PAR_DER", "WS" ]

    ruleNames = [ "IF", "ID", "NUM", "MAYOR_QUE", "PAR_IZQ", "PAR_DER", 
                  "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


