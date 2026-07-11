grammar Expr;
root: expr EOF ;

expr: ID MAYOR_IGUAL NUM ;

ID:[a-zA-Z]+[A-Za-z0-9]*;
MAYOR_IGUAL:'>=';
NUM:[0-9]+;
WS:[ \t\r\n]+ -> skip ;