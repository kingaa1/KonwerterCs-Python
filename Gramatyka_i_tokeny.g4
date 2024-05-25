grammar Gramatyka_i_tokeny;


// Parser rules
program
    : (declaration)* EOF
    ;

declaration
    :  function_definition | class_definition | statement
    ;

function_definition  
    : (variable_type | VOID) IDENTIFIER LEFTROUND RIGHTROUND LEFTCURLY 
      (statement | function_declaration)*  RIGHTCURLY   
    ;

function_declaration
    : IDENTIFIER  LEFTROUND RIGHTROUND SEMICOLON
    ;

statement
    : variable_declaration SEMICOLON
    | variable_assignment SEMICOLON
    | IF LEFTROUND expression RIGHTROUND LEFTCURLY statement* RIGHTCURLY
        (ELSE LEFTCURLY statement* RIGHTCURLY)?
    | WHILE LEFTROUND expression RIGHTROUND LEFTCURLY statement* RIGHTCURLY
    | DO LEFTCURLY statement* RIGHTCURLY
        WHILE LEFTROUND expression RIGHTROUND
        SEMICOLON
    | FOR LEFTROUND
        variable_declaration SEMICOLON
        expression SEMICOLON
        expression RIGHTROUND
        statement
    | RETURN expression SEMICOLON
    | expression SEMICOLON
    ;


variable_declaration
    : (variable_type | VAR) IDENTIFIER (EQUALS expression)? 
    ;

variable_assignment
    : IDENTIFIER EQUAL expression
    ;

variable_type
    : BOOL
    | DECIMAL
    | SHORT
    | CHAR
    | INT
    | LONG
    | FLOAT
    | DOUBLE
    ;



class_definition
    : all_member_modifier CLASS IDENTIFIER LEFTCURLY 
      (all_member_modifier? function_definition | all_member_modifier? variable_declaration SEMICOLON)+ RIGHTCURLY 
    ;


all_member_modifier
    : PUBLIC
    | PROTECTED
    | PRIVATE 
    ;


expression
    : value SEMICOLON
    ;

value
    : LEFTROUND value RIGHTROUND
    | NOT value  
    | value (EQUAL | NOTEQUAL) value
    | value (MULT | DIV | MOD) value
    | value (ADD | SUB) value
    | value (LESS | LESSOREQUAL | GREATER | GREATEROREQUAL) value
    | value AND value
    | value OR value
    | value ASSIGN value
    | value COMMA value
    | INTLIT
    | FLOATLIT
    | BOOLLIT
    | CHARLIT
    | IDENTIFIER
    ;

identifier: IDENTIFIER;


// Lexer rules
IDENTIFIER      : [a-zA-Z_] [a-zA-Z_0-9]*;
CHARLIT     : '\'' (~['\r\n] | '\\\'') '\'';
STRINGLIT   : '"' (~["\r\n] | '\\"')+ '"';
INTLIT      : [0-9]+;
FLOATLIT    : [0-9]+ '.' [0-9]+;
BOOLLIT     : ('true' | 'false');

IF              : 'if';
ELSE            : 'else';
FOR             : 'for';
WHILE           : 'while';
DO              : 'do';
RETURN          : 'return';

CHAR            : 'char';
SHORT           : 'short';
INT             : 'int';
LONG            : 'long';
FLOAT           : 'float';
DOUBLE          : 'double';
VOID            : 'void';
VAR             : 'var';
DECIMAL         : 'decimal';
BOOL            : 'bool';

ASSIGN          : '=';
ADD             : '+';
SUBSTRACT       : '-';
MULTIPLY        : '*';
DIVIDE          : '/';

EQUAL           : '==';
NOTEQUAL        : '!=';
LESS            : '<';
LESSOREQUAL     : '<=';
GREATER         : '>';
GREATEROREQUAL  : '>=';

AND             : '&&';
OR              : '||';
NOT             : '!';

LEFTROUND       : '(';
RIGHTROUND      : ')';
LEFTCURLY       : '{';
RIGHTCURLY      : '}';

SEMICOLON       : ';';
WHITESPACES     : [ \t\r\n]+ -> skip;
