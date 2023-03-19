# -*- coding:utf-8 -*-

"""Interpreter's implementation."""

from interpreter.lexer import get_token
from interpreter.parser import Parser
from interpreter.visitor import CalculationVisitor


def interpret(text):
    """Execute program.

    Args:
        text: program text

    Returns:
        result: calculation result
    """
    parser = Parser(get_token(text))
    ast = parser.parse()
    visitor = CalculationVisitor()
    return visitor.visit(ast)
