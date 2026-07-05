grammar Expr;

root: expr EOF ;    

expr: EOF;

// PALABRAS RESERVADAS
CREATE: 'CREATE';
TABLE: 'TABLE';
SERIAL: 'SERIAL';
PRIMARY: 'PRIMARY';
KEY: 'KEY';
VARCHAR: 'VARCHAR';
NOT: 'NOT';
NULL: 'NULL';
INTEGER: 'INTEGER';
DATE: 'DATE';

// IDENTIFICADORES
ID: [a-zA-Z_][a-zA-Z0-9_]* ;

// LITERALES NUMERICAS
NUM: [0-9]+;

// SIGNOS 
PAR_IZQ: '(';
PAR_DER: ')';
COMA: ',';
PUNTO_COMA: ';';

// WS (Ignorar espacios y saltos de línea)
WS: [ \t\r\n]+ -> skip ;