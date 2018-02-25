#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import antlr4

from JaRLexer import JaRLexer
from JaRListener import JaRListener
from JaRParser import JaRParser

import stack


class JaRInterpreter(JaRListener):
    def __init__(self):
        self.stack = stack.Stack()

    def exitInteger(self, ctx:JaRParser.IntegerContext):
        self.stack.push(int(ctx.NUMBER().getText()))

    def exitArith_operator(self, ctx:JaRParser.Arith_operatorContext):
        second = self.stack.pop()
        first = self.stack.pop()

        if ctx.ADD():
            self.stack.push(first + second)

        elif ctx.SUB():
            self.stack.push(first - second)

        elif ctx.MUL():
            self.stack.push(first * second)

        elif ctx.DIV():
            self.stack.push(first // second)

    def enterIf_stmt(self, ctx:JaRParser.If_stmtContext):
        second = self.stack.pop()
        first = self.stack.pop()

        if ctx.EQ():
            if first == second:
                self.stack.push(True)

            else:
                self.stack.push(False)

        elif ctx.GT():
            if first > second:
                self.stack.push(True)

            else:
                self.stack.push(False)

        elif ctx.LT():
            if first < second:
                self.stack.push(True)

            else:
                self.stack.push(False)

    # def enterCommand(self, ctx:JaRParser.CommandContext):
    #     print(self.stack)

    def exitProgram(self, ctx:JaRParser.ProgramContext):
        print(self.stack.items[-1])


if __name__ == "__main__":
    lexer = JaRLexer(antlr4.FileStream("examples/comparison.jrr"))
    stream = antlr4.CommonTokenStream(lexer)
    parser = JaRParser(stream)
    tree = parser.program()

    interpret = JaRInterpreter()
    walker = antlr4.ParseTreeWalker()
    walker.walk(interpret, tree)
