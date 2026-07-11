grammar Expr;

root: expr EOF ;

expr: PRINT PAR_IZQ CADENA PAR_DER PUNTO_COMA ;

PRINT:'print';

CADENA: '"' ~["\t\r\n]* '"' ;
PAR_IZQ:'(';
PAR_DER:')';
PUNTO_COMA:';';
WS:[ \t\r\n]+ -> skip ;