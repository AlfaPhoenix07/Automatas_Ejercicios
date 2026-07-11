grammar Expr;

root: expr EOF ;

expr: expr MAS expr MULTIPLICACION expr| MAS | MULTIPLICACION | NUM;

MAS:'+';
MULTIPLICACION:'*';
NUM:[0-9]+;
WS:[ \t\r\n]+ -> skip ;