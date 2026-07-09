grammar Expr;
root: expr EOF ;

expr: expr MAYOR_IGUAL expr | ID | NUM ;

ID:[a-zA-Z]+[A-Za-z0-9]*;

MAYOR_IGUAL:'>=';

NUM:[0-9]+;

WS:[ \t\r\n]+ -> skip ;