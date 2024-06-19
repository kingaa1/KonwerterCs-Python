import tkinter as tk
from tkinter import scrolledtext
from antlr4 import *
from antlr4.InputStream import InputStream
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException

from CSharpToPythonVisitor import CSharpToPythonVisitor
from CssGramatykaLexer import CssGramatykaLexer
from CssGramatykaParser import CssGramatykaParser
from CssGramatykaVisitor import CssGramatykaVisitor

class TreeVisitor(CssGramatykaVisitor):
    def visit(self, ctx):
        print(f"Visiting: {ctx.getText()}")
        return super().visit(ctx)

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ParseCancellationException(f"Syntax error at line {line}:{column} - {msg}")

def convert_code(csharp_code):
    try:
        input_stream = InputStream(csharp_code)
        lexer = CssGramatykaLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(MyErrorListener())

        stream = CommonTokenStream(lexer)
        parser = CssGramatykaParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(MyErrorListener())

        tree = parser.program()

        visitor = CSharpToPythonVisitor()
        python_code = visitor.visit(tree)
        return python_code

    except ParseCancellationException as e:
        return f"Parse Error: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

def on_convert_button_click():
    csharp_code = input_text.get("1.0", tk.END)
    python_code = convert_code(csharp_code)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, python_code)

# Tworzenie głównego okna
root = tk.Tk()
root.title("Konwerter C# -> Python")

# Pole tekstowe dla kodu C#
input_text = scrolledtext.ScrolledText(root, width=50, height=10, wrap=tk.WORD)
input_text.pack(pady=10)

# Przycisk do konwersji
convert_button = tk.Button(root, text="Konwertuj", command=on_convert_button_click)
convert_button.pack(pady=10)

# Pole tekstowe dla kodu Pythona
output_text = scrolledtext.ScrolledText(root, width=50, height=10, wrap=tk.WORD)
output_text.pack(pady=10)

# Uruchomienie pętli głównej aplikacji
root.mainloop()
