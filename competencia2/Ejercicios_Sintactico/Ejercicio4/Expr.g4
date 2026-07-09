grammar Expr;

root: expr EOF ;
expr: IF expr MAYOR_QUE expr | IF | ID | MAYOR_QUE | NUM;


IF:'if';
ID:[a-zA-Z]+[A-Za-z0-9]*;
IGUAL:'=';
MAYOR_QUE:'>';
NUM:[0-9]+;
WS:[ \t\r\n]+ -> skip ;