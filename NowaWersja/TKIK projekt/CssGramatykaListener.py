# Generated from CssGramatyka.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CssGramatykaParser import CssGramatykaParser
else:
    from CssGramatykaParser import CssGramatykaParser

# This class defines a complete listener for a parse tree produced by CssGramatykaParser.
class CssGramatykaListener(ParseTreeListener):

    # Enter a parse tree produced by CssGramatykaParser#program.
    def enterProgram(self, ctx:CssGramatykaParser.ProgramContext):
        pass

    # Exit a parse tree produced by CssGramatykaParser#program.
    def exitProgram(self, ctx:CssGramatykaParser.ProgramContext):
        pass


    # Enter a parse tree produced by CssGramatykaParser#declaration.
    def enterDeclaration(self, ctx:CssGramatykaParser.DeclarationContext):
        pass

    # Exit a parse tree produced by CssGramatykaParser#declaration.
    def exitDeclaration(self, ctx:CssGramatykaParser.DeclarationContext):
        pass


    # Enter a parse tree produced by CssGramatykaParser#usingStatement.
    def enterUsingStatement(self, ctx:CssGramatykaParser.UsingStatementContext):
        pass

    # Exit a parse tree produced by CssGramatykaParser#usingStatement.
    def exitUsingStatement(self, ctx:CssGramatykaParser.UsingStatementContext):
        pass


    # Enter a parse tree produced by CssGramatykaParser#variableDecDef.
    def enterVariableDecDef(self, ctx:CssGramatykaParser.VariableDecDefContext):
        pass

    # Exit a parse tree produced by CssGramatykaParser#variableDecDef.
    def exitVariableDecDef(self, ctx:CssGramatykaParser.VariableDecDefContext):
        pass


    # Enter a parse tree produced by CssGramatykaParser#functionDecDef.
    def enterFunctionDecDef(self, ctx:CssGramatykaParser.FunctionDecDefContext):
        pass

    # Exit a parse tree produced by CssGramatykaParser#functionDecDef.
    def exitFunctionDecDef(self, ctx:CssGramatykaParser.FunctionDecDefContext):
        pass


    # Enter a parse tree produced by CssGramatykaParser#classDecDef.
    def enterClassDecDef(self, ctx:CssGramatykaParser.ClassDecDefContext):
        pass

    # Exit a parse tree produced by CssGramatykaParser#classDecDef.
    def exitClassDecDef(self, ctx:CssGramatykaParser.ClassDecDefContext):
        pass


    # Enter a parse tree produced by CssGramatykaParser#statement.
    def enterStatement(self, ctx:CssGramatykaParser.StatementContext):
        pass

    # Exit a parse tree produced by CssGramatykaParser#statement.
    def exitStatement(self, ctx:CssGramatykaParser.StatementContext):
        pass


    # Enter a parse tree produced by CssGramatykaParser#expression.
    def enterExpression(self, ctx:CssGramatykaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CssGramatykaParser#expression.
    def exitExpression(self, ctx:CssGramatykaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CssGramatykaParser#value.
    def enterValue(self, ctx:CssGramatykaParser.ValueContext):
        pass

    # Exit a parse tree produced by CssGramatykaParser#value.
    def exitValue(self, ctx:CssGramatykaParser.ValueContext):
        pass


    # Enter a parse tree produced by CssGramatykaParser#type_.
    def enterType_(self, ctx:CssGramatykaParser.Type_Context):
        pass

    # Exit a parse tree produced by CssGramatykaParser#type_.
    def exitType_(self, ctx:CssGramatykaParser.Type_Context):
        pass


    # Enter a parse tree produced by CssGramatykaParser#assignOperator.
    def enterAssignOperator(self, ctx:CssGramatykaParser.AssignOperatorContext):
        pass

    # Exit a parse tree produced by CssGramatykaParser#assignOperator.
    def exitAssignOperator(self, ctx:CssGramatykaParser.AssignOperatorContext):
        pass



del CssGramatykaParser