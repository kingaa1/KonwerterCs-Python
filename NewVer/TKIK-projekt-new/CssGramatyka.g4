grammar CssGramatyka;

program
    : (usingStatement | declaration)* EOF
    ;

declaration
    : functionDecDef
    | classDecDef
    | variableDecDef
    ;

usingStatement
    : Using Identifier Semicolon
    ;


variableDecDef
    :  type_ Identifier
        (assignOperator expression)?
        Semicolon
    ;

functionDecDef
    :   Static? type_ Identifier 
        LeftRound (type_ Identifier)* RightRound
        (Semicolon | statement)
    ;

classDecDef
    : Class Identifier
        (LeftCurly (variableDecDef | functionDecDef)* RightCurly)?  
    ;


statement
    : LeftCurly 
        (variableDecDef | classDecDef | statement)*
        RightCurly
    | If LeftRound expression RightRound statement
        (Else statement)?
    | While LeftRound expression RightRound statement
    | Do statement
        While LeftRound expression RightRound
        Semicolon
    | For LeftRound
        (expression? Semicolon | variableDecDef)
        expression? Semicolon
        expression? RightRound
        statement
    | Return expression? Semicolon
    | expression Semicolon   
    ;

   
expression
    : LeftRound expression RightRound
    | (Add | Subtract | Not ) expression
    | LeftRound type_ RightRound expression
    | expression (Add | Subtract | Multiply | Divide | Modulo) expression
    | expression (Less | LessOrEqual | Greater | GreaterOrEqual) expression
    | expression (Equal | NotEqual) expression
    | expression And expression
    | expression Or expression
    | value assignOperator expression
    | value LeftRound expression? RightRound 
    | value
    | CharLiteral
    | StringLiteral
    | IntLiteral
    | FloatLiteral
    ;

assignOperator
    : Assign
    | AssignAdd
    | AssignSubtract
    | AssignMultiply
    | AssignDivide
    ;


value
    : value (Add | Subtract) expression
    | Identifier
    ;


type_
    : type_ LeftSquare IntLiteral RightSquare
    | Char           
    | Int
    | Long
    | Double
    | Float
    | Void
    | Identifier
    ;


Static          : 'static';
Char            : 'char';
Int             : 'int';
Float           : 'float';
Long            : 'long';
Double          : 'double';
Void            : 'void';

Using         : 'using';
If              : 'if';
Else            : 'else';
For             : 'for';
While           : 'while';
Do              : 'do';
Return          : 'return';
Class           : 'class';

Identifier      : [a-zA-Z_] [a-zA-Z_0-9]*;
CharLiteral     : '\'' (~['\r\n] | '\\\'') '\'';
StringLiteral   : '"' (~["\r\n] | '\\"')+ '"';
IntLiteral      : [0-9]+;
FloatLiteral    : [0-9]+ '.' [0-9]+;

Assign          : '=';
AssignAdd       : '+=';
AssignSubtract  : '-=';
AssignMultiply  : '*=';
AssignDivide    : '/=';

Add             : '+';
Subtract        : '-';
Multiply        : '*';
Divide          : '/';
Modulo          : '%';

Equal           : '==';
NotEqual        : '!=';
Less            : '<';
LessOrEqual     : '<=';
Greater         : '>';
GreaterOrEqual  : '>=';

LeftRound       : '(';
RightRound      : ')';
LeftSquare      : '[';
RightSquare     : ']';
LeftCurly       : '{';
RightCurly      : '}';

And             : '&&';
Or              : '||';
Not             : '!';

Semicolon       : ';';
Whitespace      : [ \t\r\n\f]+ -> skip;
Comment         : '//' ~[\r\n]* -> skip;