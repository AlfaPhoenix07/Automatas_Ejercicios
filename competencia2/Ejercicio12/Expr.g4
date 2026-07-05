grammar Expr;

root: expr EOF ;    

expr: EOF; 

// Palabras reservadas
PUBLIC      : 'public';
CLASS       : 'class';
STATIC      : 'static';
VOID        : 'void';
IF          : 'if';
INT         : 'int';
STRING      : 'String';

// Operadores
GE          : '>=';
ASSIGN      : '=';
PLUS        : '+';

// Delimitadores
LPAREN      : '(';
RPAREN      : ')';
LBRACE      : '{';
RBRACE      : '}';
LBRACK      : '[';
RBRACK      : ']';
SEMI        : ';';
DOT         : '.';

// Literales
INTEGER     : [0-9]+;
STRING_LITERAL
            : '"' (~["\\] | '\\' .)* '"';

// Identificadores
IDENTIFIER  : [a-zA-Z_][a-zA-Z0-9_]*;

// Espacios en blanco
WS          : [ \t\r\n]+ -> skip;