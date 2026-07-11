grammar Expr;

root: expr EOF ;

expr: NUM MAS NUM MULTIPLICACION NUM;

MAS:'+';
MULTIPLICACION:'*';
NUM:[0-9]+;
WS:[ \t\r\n]+ -> skip ;