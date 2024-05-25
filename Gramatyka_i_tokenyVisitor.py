# Generated from Gramatyka_i_tokeny.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Gramatyka_i_tokenyParser import Gramatyka_i_tokenyParser
else:
    from Gramatyka_i_tokenyParser import Gramatyka_i_tokenyParser

# This class defines a complete generic visitor for a parse tree produced by Gramatyka_i_tokenyParser.

class Gramatyka_i_tokenyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Gramatyka_i_tokenyParser#program.
    def visitProgram(self, ctx:Gramatyka_i_tokenyParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatyka_i_tokenyParser#declaration.
    def visitDeclaration(self, ctx:Gramatyka_i_tokenyParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatyka_i_tokenyParser#function_definition.
    def visitFunction_definition(self, ctx:Gramatyka_i_tokenyParser.Function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatyka_i_tokenyParser#function_declaration.
    def visitFunction_declaration(self, ctx:Gramatyka_i_tokenyParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatyka_i_tokenyParser#statement.
    def visitStatement(self, ctx:Gramatyka_i_tokenyParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatyka_i_tokenyParser#variable_declaration.
    def visitVariable_declaration(self, ctx:Gramatyka_i_tokenyParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatyka_i_tokenyParser#variable_assignment.
    def visitVariable_assignment(self, ctx:Gramatyka_i_tokenyParser.Variable_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatyka_i_tokenyParser#variable_type.
    def visitVariable_type(self, ctx:Gramatyka_i_tokenyParser.Variable_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatyka_i_tokenyParser#class_definition.
    def visitClass_definition(self, ctx:Gramatyka_i_tokenyParser.Class_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatyka_i_tokenyParser#all_member_modifier.
    def visitAll_member_modifier(self, ctx:Gramatyka_i_tokenyParser.All_member_modifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatyka_i_tokenyParser#expression.
    def visitExpression(self, ctx:Gramatyka_i_tokenyParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatyka_i_tokenyParser#value.
    def visitValue(self, ctx:Gramatyka_i_tokenyParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatyka_i_tokenyParser#identifier.
    def visitIdentifier(self, ctx:Gramatyka_i_tokenyParser.IdentifierContext):
        return self.visitChildren(ctx)



del Gramatyka_i_tokenyParser