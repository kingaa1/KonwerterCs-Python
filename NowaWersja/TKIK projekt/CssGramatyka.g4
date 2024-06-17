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
        LeftRound (type_ Identifier)? RightRound
        (Semicolon | statement)
    ;

classDecDef
    : Class Identifier
        (LeftCurly (variableDecDef | functionDecDef)* RightCurly)?  //////////////////
        Semicolon
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
    | expression (Add | Substract | Multiply | Divide | Modulo) expression
    | expression (Less | LessOrEqual | Greater | GreaterOrEqual) expression
    | expression (Equal | NotEqual) expression
    | expression And expression
    | expression Or expression
    | value assignOperator expression
    | value LeftRound expression? RightRound 
    | CharLiteral
    | StringLiteral
    | IntLiteral
    | FloatLiteral
    | value
    ;


value
    : value (Add | Subtract) expression
    | Identifier
    ;


type_
    : type_ LeftSquare IntLiteral RightSquare
    | Char            //     | Class Identifier
    | Int
    | Long
    | Double
    | Float
    | Void
    | Identifier
    ;

assignOperator
    : Assign
    | AssignAdd
    | AssignSubtract
    | AssignMultiply
    | AssignDivide
    ;

Using         : 'using';
If              : 'if';
Else            : 'else';
For             : 'for';
While           : 'while';
Do              : 'do';
Return          : 'return';
Class           : 'class';

Char            : 'char';
Int             : 'int';
Long            : 'long';
Float           : 'float';
Double          : 'double';
Void            : 'void';
Static          : 'static';

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