grammar Expr;

root: expr EOF ;    

expr: EOF;

// PALABRAS RESERVADAS
NMAP: 'nmap';
SS: 'ss';
SUDO: 'sudo';
TCPDUMP: 'tcpdump';
CURL: 'curl';
DIG: 'dig';
JOURNALCTL: 'journalctl';
GREP: 'grep';
UFW: 'ufw';

// SUBCOMANDOS
DENY: 'deny';
FROM: 'from';
TODAY: 'today';
MX: 'MX';

// BANDERAS
FLAG: '-' '-'? [a-zA-Z]+ ;

// DIRECCIONES IP 
IP: [0-9]+ '.' [0-9]+ '.' [0-9]+ '.' [0-9]+ ;

// NÚMEROS
NUM: [0-9]+ ;

// CADENAS DE TEXTO 
CADENA: '"' ~["\r\n]* '"' ;

// IDENTIFICADORES
ID: [a-zA-Z][a-zA-Z0-9.-]* ;

// SIGNOS
DIAGONAL: '/' ;

// WS
WS: [ \t\r\n]+ -> skip ;