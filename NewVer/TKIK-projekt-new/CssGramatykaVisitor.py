# Generated from CssGramatyka.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CssGramatykaParser import CssGramatykaParser
else:
    from CssGramatykaParser import CssGramatykaParser

# This class defines a complete generic visitor for a parse tree produced by CssGramatykaParser.

class CssGramatykaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CssGramatykaParser#program.
    def visitProgram(self, ctx:CssGramatykaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CssGramatykaParser#declaration.
    def visitDeclaration(self, ctx:CssGramatykaParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CssGramatykaParser#usingStatement.
    def visitUsingStatement(self, ctx:CssGramatykaParser.UsingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CssGramatykaParser#variableDecDef.
    def visitVariableDecDef(self, ctx:CssGramatykaParser.VariableDecDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CssGramatykaParser#functionDecDef.
    def visitFunctionDecDef(self, ctx:CssGramatykaParser.FunctionDecDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CssGramatykaParser#classDecDef.
    def visitClassDecDef(self, ctx:CssGramatykaParser.ClassDecDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CssGramatykaParser#statement.
    def visitStatement(self, ctx:CssGramatykaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CssGramatykaParser#expression.
    def visitExpression(self, ctx:CssGramatykaParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CssGramatykaParser#assignOperator.
    def visitAssignOperator(self, ctx:CssGramatykaParser.AssignOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CssGramatykaParser#value.
    def visitValue(self, ctx:CssGramatykaParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CssGramatykaParser#type_.
    def visitType_(self, ctx:CssGramatykaParser.Type_Context):
        return self.visitChildren(ctx)



del CssGramatykaParser