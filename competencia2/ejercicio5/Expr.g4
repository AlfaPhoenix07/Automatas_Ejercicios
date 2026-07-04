grammar Expr;

root: expr EOF;

expr: EOF;
//palabras reservadas
PRINT: 'print' ;
//cadena
CADENA: '"' ~["\r\n]* '"' ;
//White spaces
WS : [ \t\r\n]+ -> skip ;