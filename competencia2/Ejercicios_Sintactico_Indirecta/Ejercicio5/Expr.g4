grammar Expr;

root: expr EOF ;

expr: PRINT expr | PRINT | CADENA;

PRINT:'print';
CADENA: '"' ~["\r\n]* '"' ;
WS:[ \t\r\n]+ -> skip ;