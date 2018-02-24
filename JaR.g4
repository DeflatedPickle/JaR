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

command: range | arith;

// 0:5, :5 -> [0, 1, 2, 3, 4, 5]
range: NUMBER? COLON NUMBER;

arith: NUMBER+ OP=(ADD | SUB | MUL | DIV);

/*
    Lexer Rules
 */

COMMENT: '#' ~[\r\n]* -> skip;

NUMBER: [0-9]+;

// Keywords
ALPH_LOW: 'z';
ALPH_UP: 'Z';
ALPH: 'A';

// Punctuation
COLON: ':';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';