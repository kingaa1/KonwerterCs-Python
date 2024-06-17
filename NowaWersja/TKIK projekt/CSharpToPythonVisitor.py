import sys
from antlr4 import *
from CssGramatykaLexer import CssGramatykaLexer
from CssGramatykaParser import CssGramatykaParser
from CssGramatykaVisitor import CssGramatykaVisitor

class CSharpToPythonVisitor(CssGramatykaVisitor):
    def __init__(self):
        self.result = []

    def visitProgram(self, ctx: CssGramatykaParser.ProgramContext):
        for child in ctx.children:
            self.result.append(self.visit(child))
        return '\n'.join(filter(None, self.result))

    def visitUsingStatement(self, ctx: CssGramatykaParser.UsingStatementContext):
        # Ignore using statements in Python
        return ""

    def visitVariableDecDef(self, ctx: CssGramatykaParser.VariableDecDefContext):
        var_type = ctx.type_().getText()
        var_name = ctx.Identifier().getText()
        var_value = self.visit(ctx.expression()) if ctx.expression() else "None"
        return f"{var_name} = {var_value}"

    def visitFunctionDecDef(self, ctx: CssGramatykaParser.FunctionDecDefContext):
        func_name = ctx.Identifier().getText()
        param = f"{ctx.type_(0).getText()} {ctx.Identifier(0).getText()}" if ctx.type_(0) else ""
        func_body = self.visit(ctx.statement()) if ctx.statement() else "pass"
        return f"def {func_name}({param}):\n\t{func_body}"

    def visitClassDecDef(self, ctx: CssGramatykaParser.ClassDecDefContext):
        class_name = ctx.Identifier().getText()
        body = "\n".join(self.visit(child) for child in ctx.children if child != ctx.Identifier() and child != ctx.Class())
        body = body if body else "pass"
        return f"class {class_name}:\n\t{body.replace('\n', '\n\t')}"

    def visitStatement(self, ctx: CssGramatykaParser.StatementContext):
        if ctx.If():
            condition = self.visit(ctx.expression(0))
            then_stmt = self.visit(ctx.statement(0)).replace("\n", "\n\t")
            else_stmt = self.visit(ctx.statement(1)).replace("\n", "\n\t") if ctx.Else() else ""
            return f"if {condition}:\n\t{then_stmt}\nelse:\n\t{else_stmt}"
        elif ctx.expression():
            return self.visit(ctx.expression()) + "\n"
        # Handle other statement types similarly...
        return ""

    def visitExpression(self, ctx: CssGramatykaParser.ExpressionContext):
        if ctx.LeftRound() and ctx.RightRound():
            return f"({self.visit(ctx.expression(0))})"
        if ctx.value():
            return ctx.value().getText()
        if ctx.CharLiteral():
            return ctx.CharLiteral().getText()
        if ctx.StringLiteral():
            return ctx.StringLiteral().getText()
        if ctx.IntLiteral():
            return ctx.IntLiteral().getText()
        if ctx.FloatLiteral():
            return ctx.FloatLiteral().getText()
        # Handle other expressions...
        return ""

def convert_csharp_to_python(input_code):
    input_stream = InputStream(input_code)
    lexer = CssGramatykaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CssGramatykaParser(stream)
    tree = parser.program()

    visitor = CSharpToPythonVisitor()
    python_code = visitor.visit(tree)
    return python_code

# Example usage
if __name__ == '__main__':
    csharp_code = """
    using System;
    class Test {
        int x = 5;
        void foo() {
            if (x > 0) {
                x -= 1;
            }
        }
    }
    """
    python_code = convert_csharp_to_python(csharp_code)
    print(python_code)
