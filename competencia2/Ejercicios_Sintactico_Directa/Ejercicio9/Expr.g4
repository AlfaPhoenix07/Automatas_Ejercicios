grammar Expr;


root: expr EOF ;

expr: IF PAR_IZQ ID MAYOR_QUE NUM PAR_DER ;


IF:'if';
ID:[a-zA-Z]+[A-Za-z0-9]*;
NUM:[0-9]+;
MAYOR_QUE:'>';
PAR_IZQ:'(';
PAR_DER:')';


WS:[ \t\r\n]+ -> skip ;