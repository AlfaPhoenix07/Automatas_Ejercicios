grammar Expr;

root: expr EOF;

expr: EOF;
//palabras reservadas
IF: 'if' ;
//identificadores
ID: [a-zA-Z_][a-zA-Z0-9_]* ;
//literales numericas
NUM: [0-9]+ ;
//signos
PAR_IZQ: '(' ;
PAR_DER: ')' ;
//signos de comparacion
MAYOR: '>' ;
//White spaces
WS : [ \t\r\n]+ -> skip ;