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
        var_type = ctx.type_().getText()
        var_name = str(ctx.Identifier())                     #  ctx.Identifier().getText()
        var_value = self.visit(ctx.expression()) if ctx.expression() else "None"
        return f"{var_name} = {var_value}"

    


    def visitFunctionDecDef(self, ctx: CssGramatykaParser.FunctionDecDefContext):  ########
        func_name = str(ctx.Identifier(0))                # ctx.Identifier().getText()   # 0
        params = []

        if ctx.type_(0):
            # dodać iterację ?
            param_name =  str(ctx.Identifier(1))                        #  ctx.Identifier().getText() # 1
            params.append(f"{param_name}")  # Ignore type for Python
        func_body = self.visit(ctx.statement()) if ctx.statement() else "pass"
        func_body_formatted = func_body.replace('\n', '\n\t')
        return f"def {func_name}({', '.join(params)}):\n\t{func_body_formatted}"




    # def visitClassDecDef(self, ctx: CssGramatykaParser.ClassDecDefContext):
    #     class_name = ctx.Identifier().getText()
    #     body = "\n".join(self.visit(child) for child in ctx.children if child != ctx.Identifier() and child != ctx.Class())
    #     body = body if body else "pass"
    #     return f"class {class_name}:\n\t{body.replace('\n', '\n\t')}"

    def visitClassDecDef(self, ctx: CssGramatykaParser.ClassDecDefContext,  tabs=0):
        print("class "+str(ctx.Identifier()), end="")
        class_name = ctx.Identifier().getText()

        print(":")
        #print("\t")
        
        object_types = [type(obj).__name__ for obj in ctx.children]
        #print(object_types)
        default = True
        for i in range(len(ctx.children)):
            if default and object_types[i] != "TerminalNodeImpl": 
                func = getattr(CSharpToPythonVisitor, "visit"+object_types[i].replace("Context", ""))
                if "visitFunctionDecDef" in str(func):  # + DecDef
                    tabs_ = ""
                    for i in range(tabs):
                        tabs_ += "    "
                    print(tabs_, end="")
                    #print("def ", end="")
                    CSharpToPythonVisitor.visitFunctionDecDef(self, ctx.children[i])
                elif "visitVariableDecDef" in str(func):   # + DecDef
                    tabs_ = ""
                    for i in range(tabs):
                        tabs_ += "    "
                    print(tabs_, end="")
                    print(CSharpToPythonVisitor.visitVariableDecDef(self, ctx.children[i]))
                    func(self, ctx.children[i])
                    print()
                elif "visitStatement" in str(func):
                    print(CSharpToPythonVisitor.visitStatement(self, ctx.children[i]))


    def visitStatement(self, ctx: CssGramatykaParser.StatementContext):
        if ctx.LeftCurly():
            statements = "\n".join(self.visit(child) for child in ctx.children if child not in [ctx.LeftCurly(), ctx.RightCurly()])
            return f"{statements}"
        if ctx.If():
            condition = self.visit(ctx.expression(0))
            then_stmt = self.visit(ctx.statement(0)).replace("\n", "\n\t")
            else_stmt = self.visit(ctx.statement(1)).replace("\n", "\n\t") if ctx.Else() else ""
            return f"if {condition}:\n\t{then_stmt}\nelse:\n\t{else_stmt}" if ctx.Else() else f"if {condition}:\n\t{then_stmt}"
        if ctx.While():
            condition = self.visit(ctx.expression(0))
            body = self.visit(ctx.statement(0)).replace("\n", "\n\t")
            return f"while {condition}:\n\t{body}"
        if ctx.Do():
            body = self.visit(ctx.statement(0)).replace("\n", "\n\t")
            condition = self.visit(ctx.expression(0))
            return f"while True:\n\t{body}\n\tif not ({condition}):\n\t\tbreak"
        if ctx.For():
            init = self.visit(ctx.variableDecDef()) if ctx.variableDecDef() else self.visit(ctx.expression(0))
            condition = self.visit(ctx.expression(1))
            increment = self.visit(ctx.expression(2))
            body = self.visit(ctx.statement(0)).replace("\n", "\n\t")
            return f"{init}\nwhile {condition}:\n\t{body}\n\t{increment}"
        if ctx.Return():
            return f"return {self.visit(ctx.expression(0))}" if ctx.expression(0) else "return"
        if ctx.expression():
            return self.visit(ctx.expression()) + "\n"
        return ""

    def visitExpression(self, ctx: CssGramatykaParser.ExpressionContext):
        if ctx.LeftRound() and ctx.RightRound():
            return f"({self.visit(ctx.expression(0))})"
        if ctx.Add() or ctx.Subtract() or ctx.Not():
            operator = ctx.Add().getText() if ctx.Add() else ctx.Subtract().getText() if ctx.Subtract() else ctx.Not().getText()
            return f"{operator}{self.visit(ctx.expression(0))}"
        if ctx.LeftRound() and ctx.RightRound() and ctx.type_():
            return f"({self.visit(ctx.type_())}){self.visit(ctx.expression(0))}"
        if ctx.value() and ctx.assignOperator():
            return f"{self.visit(ctx.value())} {ctx.assignOperator().getText()} {self.visit(ctx.expression(0))}"
        if ctx.value() and ctx.LeftRound() and ctx.RightRound():
            func_call = f"{self.visit(ctx.value())}({self.visit(ctx.expression(0)) if ctx.expression(0) else ''})"
            return func_call
        if ctx.value():
            return self.visit(ctx.value())
        if ctx.CharLiteral():
            return ctx.CharLiteral().getText()
        if ctx.StringLiteral():
            return ctx.StringLiteral().getText()
        if ctx.IntLiteral():
            return ctx.IntLiteral().getText()
        if ctx.FloatLiteral():
            return ctx.FloatLiteral().getText()
        if ctx.Identifier() and ctx.LeftRound():
            func_call = f"{ctx.Identifier().getText()}({self.visit(ctx.expression(0)) if ctx.expression(0) else ''})"
            return func_call
        if ctx.Identifier():
            return ctx.Identifier().getText()
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
        return ""



# import sys
# from antlr4 import *
# from CssGramatykaLexer import CssGramatykaLexer
# from CssGramatykaParser import CssGramatykaParser
# from CssGramatykaVisitor import CssGramatykaVisitor

# class CSharpToPythonVisitor(CssGramatykaVisitor):
#     def __init__(self):
#         self.result = []

#     def visitProgram(self, ctx: CssGramatykaParser.ProgramContext):
#         for child in ctx.children:
#             self.result.append(self.visit(child))
#         return '\n'.join(filter(None, self.result))

#     def visitUsingStatement(self, ctx: CssGramatykaParser.UsingStatementContext):
#         # Ignore using statements in Python
#         return ""

#     def visitVariableDecDef(self, ctx: CssGramatykaParser.VariableDecDefContext):
#         var_type = ctx.type_().getText()
#         var_name = ctx.Identifier().getText()
#         var_value = self.visit(ctx.expression()) if ctx.expression() else "None"
#         return f"{var_name} = {var_value}"

#     def visitFunctionDecDef(self, ctx: CssGramatykaParser.FunctionDecDefContext):
#         func_name = ctx.Identifier().getText()
#         param = f"{ctx.type_(0).getText()} {ctx.Identifier(0).getText()}" if ctx.type_(0) else ""
#         func_body = self.visit(ctx.statement()) if ctx.statement() else "pass"
#         return f"def {func_name}({param}):\n\t{func_body}"

#     def visitClassDecDef(self, ctx: CssGramatykaParser.ClassDecDefContext):
#         class_name = ctx.Identifier().getText()
#         body = "\n".join(self.visit(child) for child in ctx.children if child != ctx.Identifier() and child != ctx.Class())
#         body = body if body else "pass"
#         return f"class {class_name}:\n\t{body.replace('\n', '\n\t')}"

#     def visitStatement(self, ctx: CssGramatykaParser.StatementContext):
#         if ctx.If():
#             condition = self.visit(ctx.expression(0))
#             then_stmt = self.visit(ctx.statement(0)).replace("\n", "\n\t")
#             else_stmt = self.visit(ctx.statement(1)).replace("\n", "\n\t") if ctx.Else() else ""
#             return f"if {condition}:\n\t{then_stmt}\nelse:\n\t{else_stmt}"
#         elif ctx.expression():
#             return self.visit(ctx.expression()) + "\n"
#         # Handle other statement types similarly...
#         return ""

#     def visitExpression(self, ctx: CssGramatykaParser.ExpressionContext):
#         if ctx.LeftRound() and ctx.RightRound():
#             return f"({self.visit(ctx.expression(0))})"
#         if ctx.value():
#             return ctx.value().getText()
#         if ctx.CharLiteral():
#             return ctx.CharLiteral().getText()
#         if ctx.StringLiteral():
#             return ctx.StringLiteral().getText()
#         if ctx.IntLiteral():
#             return ctx.IntLiteral().getText()
#         if ctx.FloatLiteral():
#             return ctx.FloatLiteral().getText()
#         # Handle other expressions...
#         return ""

# def convert_csharp_to_python(input_code):
#     input_stream = InputStream(input_code)
#     lexer = CssGramatykaLexer(input_stream)
#     stream = CommonTokenStream(lexer)
#     parser = CssGramatykaParser(stream)
#     tree = parser.program()

#     visitor = CSharpToPythonVisitor()
#     python_code = visitor.visit(tree)
#     return python_code

# # Example usage
# if __name__ == '__main__':
#     csharp_code = """
#     using System;
#     class Test {
#         int x = 5;
#         void foo() {
#             if (x > 0) {
#                 x -= 1;
#             }
#         }
#     }
#     """
#     python_code = convert_csharp_to_python(csharp_code)
#     print(python_code)


