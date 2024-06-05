from antlr4 import *
from Gramatyka_i_tokenyLexer import Gramatyka_i_tokenyLexer
from Gramatyka_i_tokenyParser import Gramatyka_i_tokenyParser
from Gramatyka_i_tokenyVisitor import Gramatyka_i_tokenyVisitor

def main():
    expression = input("Enter an expression: ")
    input_stream = InputStream(expression)
    lexer = Gramatyka_i_tokenyLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Gramatyka_i_tokenyParser(token_stream)
    tree = parser.program()
    
    result = tree.parser()
    return result

r = main()
print(r)