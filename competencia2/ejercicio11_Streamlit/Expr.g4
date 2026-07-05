grammar Expr;

root: expr EOF ;    

expr: EOF;
 //PALABRAS RESERVADAS
PUBLIC: 'public' ;
CLASS: 'class' ;
STATIC: 'static';
VOID: 'void';
INT: 'int' ;
DOUBLE: 'double' ;
STRING: 'string' ;
BOOLEAN: 'boolean';
FOR: 'for';
WHILE:'while';
DO:'do';
GET:'get' ;
SET:'set' ;
NEW:'new' ;
SCANNER:'Scanner';
IF:'if' ;
ELSE:'else' ;
IMPORT:'import';
PRIVATE:'private';
THIS:'this';
NULL:'null';
TRUE:'true';
FALSE:'false';


//identificadores
ID:[a-zA-Z_]+[a-zA-Z0-9]* ;
//literales numericas
NUM:[0-9]+;

//cadena
CADENA: '"' ~["\r\n]* '"' ;

//signos 
IGUAL:'=';
IGUAL_IGUAL:'==';
MAS:'+';
MENOS:'-';
MULTI:'*';
MODULO:'%';
DIVISION:'/';
MAYOR:'>';
MENOR:'<';
MAYOR_IGUAL:'>=';
MENOR_IGUAL:'<=';
MAS_MAS:'++';
MENOS_MENOS:'--';
PAR_IZQ:'(';
PAR_DER:')';
LLAVE_IZQ:'{';
LLAVE_DER:'}';
PUNTO_COMA:';';
DOS_PUNTOS:':';
PUNTO:'.';
COR_IZQ:'[';
COR_DER:']';


//WS
WS: [ \t\r\n]+ -> skip ;