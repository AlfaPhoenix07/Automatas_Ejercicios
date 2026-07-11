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
        4,0,5,40,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,
        0,1,0,1,1,4,1,17,8,1,11,1,12,1,18,1,1,5,1,22,8,1,10,1,12,1,25,9,
        1,1,2,4,2,28,8,2,11,2,12,2,29,1,3,1,3,1,4,4,4,35,8,4,11,4,12,4,36,
        1,4,1,4,0,0,5,1,1,3,2,5,3,7,4,9,5,1,0,4,2,0,65,90,97,122,3,0,48,
        57,65,90,97,122,1,0,48,57,3,0,9,10,13,13,32,32,43,0,1,1,0,0,0,0,
        3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,1,11,1,0,0,0,3,16,
        1,0,0,0,5,27,1,0,0,0,7,31,1,0,0,0,9,34,1,0,0,0,11,12,5,105,0,0,12,
        13,5,110,0,0,13,14,5,116,0,0,14,2,1,0,0,0,15,17,7,0,0,0,16,15,1,
        0,0,0,17,18,1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,0,19,23,1,0,0,0,20,
        22,7,1,0,0,21,20,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,
        0,24,4,1,0,0,0,25,23,1,0,0,0,26,28,7,2,0,0,27,26,1,0,0,0,28,29,1,
        0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,6,1,0,0,0,31,32,5,61,0,0,32,
        8,1,0,0,0,33,35,7,3,0,0,34,33,1,0,0,0,35,36,1,0,0,0,36,34,1,0,0,
        0,36,37,1,0,0,0,37,38,1,0,0,0,38,39,6,4,0,0,39,10,1,0,0,0,5,0,18,
        23,29,36,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    ID = 2
    NUM = 3
    IGUAL = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "INT", "ID", "NUM", "IGUAL", "WS" ]

    ruleNames = [ "INT", "ID", "NUM", "IGUAL", "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


