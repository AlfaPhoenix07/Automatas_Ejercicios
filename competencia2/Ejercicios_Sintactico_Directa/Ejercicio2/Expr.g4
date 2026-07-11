grammar Expr;

root: expr EOF ;

expr: NUM MENOS NUM ;

MENOS:'-';

NUM:[0-9]+;

WS:[ \t\r\n]+ -> skip ;