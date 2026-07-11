grammar Expr;

root: expr EOF ;

expr: INT expr IGUAL expr | INT | ID | IGUAL | NUM;

INT:'int';
ID:[a-zA-Z]+[A-Za-z0-9]*;
NUM:[0-9]+;
IGUAL:'=';

WS:[ \t\r\n]+ -> skip ;