grammar Expr;

root: expr EOF ;

expr: EOF;

// Palabras reservadas
UPDATE      : 'UPDATE';
SET         : 'SET';
WHERE       : 'WHERE';

// Operadores
ASSIGN      : '=';
COMMA       : ',';
SEMI        : ';';

// Literales
INTEGER     : [0-9]+;
STRING      : '\'' (~['\\] | '\\' .)* '\'';

// Identificadores
IDENTIFIER  : [a-zA-Z_][a-zA-Z0-9_]*;

// Espacios en blanco
WS          : [ \t\r\n]+ -> skip;