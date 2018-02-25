grammar JaR;

options {
    language=Python3;
}

/*
    Parser Rules
 */

program: code EOF;
code: line+;
line: COMMENT | command+;

command: range_ | integer | if_stmt | arith_operator;

// 0:5, :5 -> [0, 1, 2, 3, 4, 5]
range_: RANGE;

integer: NUMBER;

if_stmt: IF (EQ | GT | LT | GTE | LTE);

// arith: NUMBER+ OP=(ADD | SUB | MUL | DIV);
arith_operator: ADD | SUB | MUL | DIV;

/*
    Lexer Rules
 */

COMMENT: '#' ~[\r\n]* -> skip;

RANGE: NUMBER? COLON NUMBER;

NUMBER: [0-9]+ | RANDOM;

// Keywords
ALPH_LOW: 'z';
ALPH_UP: 'Z';
ALPH: 'A';

FOR: 'A';
FORALL: 'E';

IF: '?';

EQ: '=';
GT: '>';
LT: '<';

GTE: '>=';
LTE: '<=';

NEQ: '!=';
NGT: '!>';
NLT: '!<';

OR: '|';

LOOP: '@';

RANDOM: 'r';

// Punctuation
COLON: ':';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

// Other
WS: [ \t\r\n\f]+ -> skip;