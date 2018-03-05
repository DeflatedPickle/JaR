#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import random

import antlr4
from antlr4.tree import Tree

from JaRLexer import JaRLexer
from JaRListener import JaRListener
from JaRParser import JaRParser
from util import stack, prime


class JaRInterpreter(JaRListener):
    def __init__(self):
        self.stack = stack.Stack()

        self.variables = {}

    def enterPrint_(self, ctx:JaRParser.Print_Context):
        print(self.stack.items[-1])

    def exitInteger(self, ctx:JaRParser.IntegerContext):
        self.stack.push(int(ctx.NUMBER().getText()) if ctx.NUMBER().getText() != "r" else random.randint(0, 100))

    def exitRange_(self, ctx:JaRParser.Range_Context):
        new_ctx = ctx.getText().split(":")
        second = int(new_ctx[-1])
        first = (int(new_ctx[0]) if new_ctx[0] != "" else 0) if new_ctx[0] != "r" else random.randint(0, second)

        self.stack.push(range(first, second))

    def enterPrime(self, ctx:JaRParser.PrimeContext):
        if prime.is_prime(self.stack.pop()):
            self.stack.push(True)

        else:
            self.stack.push(False)

    def enterInput_(self, ctx:JaRParser.Input_Context):
        in_ = input()

        try:
            self.stack.push(int(in_))

        except ValueError:
            self.stack.push(in_)

    def enterVariable(self, ctx:JaRParser.VariableContext):
        self.variables[ctx.VARIABLE()] = self.stack.pop()
        self.stack.push(ctx.VARIABLE())

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

        elif ctx.GTE():
            if first >= second:
                self.stack.push(True)

            else:
                self.stack.push(False)

        elif ctx.LTE():
            if first < second:
                self.stack.push(True)

            else:
                self.stack.push(False)

    def enterFor_all_block(self, ctx:JaRParser.For_all_blockContext):
        looper = self.stack.pop()

        if type(looper) != range:
            looper = range(0, looper)

        for _ in looper:
            for line in ctx.line():
                # self.visitTerminal(line)
                Tree.ParseTreeVisitor().visitChildren(line)

    def enterCommand(self, ctx:JaRParser.CommandContext):
        print(self.stack)

    def exitProgram(self, ctx:JaRParser.ProgramContext):
        stack = self.stack.items[-1]

        if type(stack) is int:
            print(stack)

        elif type(stack) is bool:
            print(stack)

        else:
            print(self.variables[stack])


if __name__ == "__main__":
    lexer = JaRLexer(antlr4.FileStream("examples/input.jrr"))
    stream = antlr4.CommonTokenStream(lexer)
    parser = JaRParser(stream)
    tree = parser.program()

    interpret = JaRInterpreter()
    walker = antlr4.ParseTreeWalker()
    walker.walk(interpret, tree)
