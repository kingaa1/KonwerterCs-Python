import sys
from antlr4 import *
from CssGramatykaLexer import CssGramatykaLexer
from CssGramatykaParser import CssGramatykaParser
from CSharpToPythonVisitor import CSharpToPythonVisitor

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = CssGramatykaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CssGramatykaParser(stream)
    tree = parser.program()

    visitor = CSharpToPythonVisitor()
    output = visitor.visit(tree)
    print(output)

if __name__ == '__main__':
    main(sys.argv)
