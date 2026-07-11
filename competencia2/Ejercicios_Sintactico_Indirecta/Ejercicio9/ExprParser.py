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
        4,1,7,20,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,3,1,18,8,1,1,1,0,0,2,0,2,0,0,20,0,4,1,0,0,0,2,17,1,0,
        0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,8,5,1,0,0,8,9,5,5,0,0,
        9,10,3,2,1,0,10,11,5,4,0,0,11,12,3,2,1,0,12,13,5,6,0,0,13,18,1,0,
        0,0,14,18,5,2,0,0,15,18,5,3,0,0,16,18,1,0,0,0,17,7,1,0,0,0,17,14,
        1,0,0,0,17,15,1,0,0,0,17,16,1,0,0,0,18,3,1,0,0,0,1,17
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "<INVALID>", "<INVALID>", "'>'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "IF", "ID", "NUM", "MAYOR_QUE", "PAR_IZQ", 
                      "PAR_DER", "WS" ]

    RULE_root = 0
    RULE_expr = 1

    ruleNames =  [ "root", "expr" ]

    EOF = Token.EOF
    IF=1
    ID=2
    NUM=3
    MAYOR_QUE=4
    PAR_IZQ=5
    PAR_DER=6
    WS=7

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

        def IF(self):
            return self.getToken(ExprParser.IF, 0)

        def PAR_IZQ(self):
            return self.getToken(ExprParser.PAR_IZQ, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def MAYOR_QUE(self):
            return self.getToken(ExprParser.MAYOR_QUE, 0)

        def PAR_DER(self):
            return self.getToken(ExprParser.PAR_DER, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 7
                self.match(ExprParser.IF)
                self.state = 8
                self.match(ExprParser.PAR_IZQ)
                self.state = 9
                self.expr()
                self.state = 10
                self.match(ExprParser.MAYOR_QUE)
                self.state = 11
                self.expr()
                self.state = 12
                self.match(ExprParser.PAR_DER)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(ExprParser.ID)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 15
                self.match(ExprParser.NUM)
                pass
            elif token in [-1, 4, 6]:
                self.enterOuterAlt(localctx, 4)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





