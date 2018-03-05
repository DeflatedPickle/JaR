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

command: range_
       | prime
       | integer | variable
       | if_stmt | arith_operator
       | for_all_block | ITEM
       | print_ | input_;

print_: PRINT;
input_: INPUT;

prime: PRIME;

// 0:5, :5 -> [0, 1, 2, 3, 4, 5]
range_: RANGE;

integer: NUMBER;

variable: VARIABLE;

if_stmt: IF (EQ | GT | LT | GTE | LTE);

// arith: NUMBER+ OP=(ADD | SUB | MUL | DIV);
arith_operator: ADD | SUB | MUL | DIV;

for_all_block: FORALL OBLOCK line* CBLOCK;

/*
    Lexer Rules
 */

COMMENT: '#' ~[\r\n]* -> skip;

RANGE: NUMBER? COLON NUMBER;

NUMBER: [0-9]+ | RANDOM;

// Keywords
// ALPH_LOW: 'z';
// ALPH_UP: 'Z';
// ALPH: 'A';

PRIME: 'P';

FORALL: 'A';

ITEM: 'i';

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

PRINT: '`';
INPUT: '~';

VARIABLE: [a-z];

// Punctuation
COLON: ':';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

OBLOCK: '{';
CBLOCK: '}';

// Other
WS: [ \t\r\n\f]+ -> skip;