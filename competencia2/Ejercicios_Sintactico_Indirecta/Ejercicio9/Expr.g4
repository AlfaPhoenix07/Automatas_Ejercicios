grammar Expr;


root: expr EOF ;

expr: IF PAR_IZQ expr MAYOR_QUE expr PAR_DER | ID | NUM | ;


IF:'if';
ID:[a-zA-Z]+[A-Za-z0-9]*;
NUM:[0-9]+;
MAYOR_QUE:'>';
PAR_IZQ:'(';
PAR_DER:')';


WS:[ \t\r\n]+ -> skip ;