import antlr4

from JaRLexer import JaRLexer
from JaRListener import JaRListener
from JaRParser import JaRParser


class JaRInterpreter(JaRListener):
    def __init__(self):
        pass


if __name__ == "__main__":
    lexer = JaRLexer(antlr4.FileStream("examples/range.jrr"))
    stream = antlr4.CommonTokenStream(lexer)
    parser = JaRParser(stream)
    tree = parser.program()

    interpret = JaRInterpreter()
    walker = antlr4.ParseTreeWalker()
    walker.walk(interpret, tree)
