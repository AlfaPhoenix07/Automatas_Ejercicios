grammar Expr;

root: expr EOF;

expr: EOF;
//identificadores
ID: [a-zA-Z_][a-zA-Z0-9_]* ;
//literales numericas
NUM: [0-9]+ ;
//operadores de asignacion
IGUAL: '=' ;


WS : [ \t\r\n]+ -> skip ;