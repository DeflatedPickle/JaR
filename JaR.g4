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

integer: NUMBER;
// 0:5, :5 -> [0, 1, 2, 3, 4, 5]
range_: RANGE;

if_stmt: IF (EQ | GT | LT);

// arith: NUMBER+ OP=(ADD | SUB | MUL | DIV);
arith_operator: ADD | SUB | MUL | DIV;

/*
    Lexer Rules
 */

COMMENT: '#' ~[\r\n]* -> skip;

RANGE: NUMBER? COLON NUMBER;

NUMBER: [0-9]+;

// Keywords
ALPH_LOW: 'z';
ALPH_UP: 'Z';
ALPH: 'A';

IF: '?';

EQ: 'e';
GT: 'g';
LT: 'l';

OR: 'o';

RANDOM: 'r';

// Punctuation
COLON: ':';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

// Other
WS: [ \t\r\n\f]+ -> skip;