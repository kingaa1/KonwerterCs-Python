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
        return ""

    def visitVariableDecDef(self, ctx: CssGramatykaParser.VariableDecDefContext):
        var_name = str(ctx.Identifier())
        var_value = self.visit(ctx.expression()) if ctx.expression() else "None"
        return f"{var_name} = {var_value}"

    def visitFunctionDecDef(self, ctx: CssGramatykaParser.FunctionDecDefContext):
        func_name = str(ctx.Identifier(0))
        params = []

        if ctx.type_(0):
            if (str(ctx.Identifier(1))!='None'):
                param_name = str(ctx.Identifier(1))
                params.append(f"{param_name}")  # Ignore type for Python
            if (str(ctx.Identifier(2))!='None'):
                param_name2 = str(ctx.Identifier(2))
                params.append(f"{param_name2}")  # Ignore type for Python
            if (str(ctx.Identifier(3))!='None'):
                param_name2 = str(ctx.Identifier(3))
                params.append(f"{param_name2}")  # Ignore type for Python
        
        func_body = self.visit(ctx.statement()) if ctx.statement() else "pass"
        func_body_formatted = func_body.replace('\n', '\n    ')
        return f"def {func_name}({', '.join(params)}):\n\t{func_body_formatted}"

    def visitClassDecDef(self, ctx: CssGramatykaParser.ClassDecDefContext, tabs=0):
        class_name = str(ctx.Identifier())
        result = [f"class {class_name}:"]
        
        for child in ctx.children:
            child_type = type(child).__name__
            if child_type != "TerminalNodeImpl":
                method_name = "visit" + child_type.replace("Context", "")
                if hasattr(self, method_name):
                    visitor = getattr(self, method_name)
                    child_result = visitor(child)
                    if child_result:
                        indented_result = "\n".join(["    " + line for line in child_result.split("\n")])
                        result.append(indented_result)
        
        self.result.append("\n".join(result))
        return ""

    def visitStatement(self, ctx: CssGramatykaParser.StatementContext):
        if ctx.LeftCurly() and ctx.RightCurly():
            statements = "\n".join(self.visit(child) for child in ctx.children if child not in [ctx.LeftCurly(), ctx.RightCurly()])
            return f"{statements}"
        if ctx.If():
            if ctx.If():
                condition = self.visit(ctx.expression(0))
                then_stmt = self.visit(ctx.statement(0)).replace("\n", "\n    ")
                else_stmt = self.visit(ctx.statement(1)).replace("\n", "\n    ") if ctx.Else() else ""
                return f"if {condition}:\n    {then_stmt}\nelse:\n    {else_stmt}"
        if ctx.While():
            condition = self.visit(ctx.expression(0))
            body = self.visit(ctx.statement(0)).replace("\n", "\n\t")
            return f"while ({condition}):\n\t{body}"
        if ctx.Do():
            body = self.visit(ctx.statement(0)).replace("\n", "\n\t")
            condition = self.visit(ctx.expression(0))
            return f"while True:\n\t{body}\n\tif not ({condition}):\n\t\tbreak"
        if ctx.For():
            init = self.visit(ctx.expression(0))
            condition = self.visit(ctx.expression(1))
            increment = self.visit(ctx.expression(2))
            body = self.visit(ctx.statement(0)).replace("\n", "\n    ")
            if init.startswith("int"):
                var_name, start = init.replace("int ", "").split("=")
                start = start.strip()
                end = condition.split("<")[1].strip()
                return f"for {var_name.strip()} in range({start}, {end}):\n    {body}\n    {increment}"
            else:
                return f"{init}\nwhile {condition}:\n    {body}\n    {increment}"
        if ctx.Return():
            return f"return {self.visit(ctx.expression(0))}" if ctx.expression(0) else "return"
        if ctx.expression():
            return self.visit(ctx.expression()) + "\n"
        return ""

    def visitExpression(self, ctx: CssGramatykaParser.ExpressionContext):
        # Handle parenthesized expressions
        if ctx.LeftRound() and ctx.RightRound():
            if ctx.expression(0):
                return f"({self.visit(ctx.expression(0))})"
            elif ctx.type_():
                return f"({self.visit(ctx.type_())}){self.visit(ctx.expression(1))}"
        
        # Handle unary operators (Add, Subtract, Not)
        if ctx.Add() or ctx.Subtract() or ctx.Not():
            operator = ctx.Add().getText() if ctx.Add() else ctx.Subtract().getText() if ctx.Subtract() else "not"
            return f"{operator} {self.visit(ctx.expression(0))}"
        
        # Handle binary operators (+, -, *, /, %)
        if ctx.expression(0) and ctx.expression(1):
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            if ctx.Add():
                return f"{left} + {right}"
            elif ctx.Subtract():
                return f"{left} - {right}"
            elif ctx.Multiply():
                return f"{left} * {right}"
            elif ctx.Divide():
                return f"{left} / {right}"
            elif ctx.Modulo():
                return f"{left} % {right}"
            elif ctx.Less():
                return f"{left} < {right}"
            elif ctx.LessOrEqual():
                return f"{left} <= {right}"
            elif ctx.Greater():
                return f"{left} > {right}"
            elif ctx.GreaterOrEqual():
                return f"{left} >= {right}"
            elif ctx.Equal():
                return f"{left} == {right}"
            elif ctx.NotEqual():
                return f"{left} != {right}"
            elif ctx.And():
                return f"{left} and {right}"
            elif ctx.Or():
                return f"{left} or {right}"
        
        # Handle assignment
        if ctx.value() and ctx.assignOperator():
            return f"{self.visit(ctx.value())} {self.visit(ctx.assignOperator())} {self.visit(ctx.expression(0))}"
        
        # Handle function calls
        if ctx.value() and ctx.LeftRound() and ctx.RightRound():
            func_name = self.visit(ctx.value())
            arg = self.visit(ctx.expression(0)) if ctx.expression(0) else ""
            return f"{func_name}({arg})"
        
        # Handle literals and values
        if ctx.CharLiteral():
            return ctx.CharLiteral().getText()
        if ctx.StringLiteral():
            return ctx.StringLiteral().getText()
        if ctx.IntLiteral():
            return ctx.IntLiteral().getText()
        if ctx.FloatLiteral():
            return ctx.FloatLiteral().getText()
        if ctx.value():
            return self.visit(ctx.value())
        
        return ""


    def visitValue(self, ctx: CssGramatykaParser.ValueContext):
        if ctx.Identifier():
            return ctx.Identifier().getText()
        return ""

    def visitType_(self, ctx: CssGramatykaParser.Type_Context):
        if ctx.Char():
            return 'str'
        if ctx.Int():
            return 'int'
        if ctx.Long():
            return 'int'
        if ctx.Float():
            return 'float'
        if ctx.Double():
            return 'float'
        if ctx.Void():
            return 'None'
        if ctx.Identifier():
            return ctx.Identifier().getText()
        if ctx.LeftSquare() and ctx.RightSquare():
            return f"{self.visit(ctx.type_())}[]"
        return ""

    def visitAssignOperator(self, ctx: CssGramatykaParser.AssignOperatorContext):
        if ctx.Assign():
            return '='
        if ctx.AssignAdd():
            return '+='
        if ctx.AssignSubtract():
            return '-='
        if ctx.AssignMultiply():
            return '*='
        if ctx.AssignDivide():
            return '/='
        return ctx.getText()