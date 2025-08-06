import sys
from antlr4 import *
from MiniLangLexer import MiniLangLexer
from MiniLangParser import MiniLangParser

def main():
    input_stream = FileStream("prueba.txt", encoding="utf-8")  # Ensure the file path is correct
    lexer = MiniLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniLangParser(stream)
    tree = parser.prog()  # We are using 'prog' since this is the starting rule based on our MiniLang grammar, yay!
    print("Parse tree:", tree.toStringTree(recog=parser))  


main()