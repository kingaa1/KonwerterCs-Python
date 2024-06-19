import sys
from antlr4 import *
from CssGramatykaLexer import CssGramatykaLexer
from CssGramatykaParser import CssGramatykaParser
from CssGramatykaVisitor import CssGramatykaVisitor

from CSharpToPythonVisitor import CSharpToPythonVisitor

class TreeVisitor(CssGramatykaVisitor):
    def visit(self, ctx):
        print(f"Visiting: {ctx.getText()}")
        return super().visit(ctx)


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


