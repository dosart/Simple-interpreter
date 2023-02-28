# -*- coding:utf-8 -*-

"""Implementing a Visitor template for AST."""

from functools import singledispatch

from interpreter.ast import BinaryOperation, Num
from interpreter.token import TokenType


@singledispatch
def visit(node):
    """Raise error.

    Args:
        node: unknown type

    Raises:
        AttributeError: raise exception
    """
    type_name = type(node).__name__
    raise AttributeError("No handler found for {type_name}".format(type_name=type_name))


@visit.register(Num)
def visit(node):
    """Visit Num node and return value.

    Args:
        node: integer

    Returns:
        value: calculation result
    """
    return node.value


@visit.register(BinaryOperation)
def visit(node):
    """Visit BinaryOperation node and return calculation result.

    Args:
        node: bynary operation

    Returns:
        value: calculation result
    """
    if node.op.type == TokenType.plus:
        return visit(node.left) + visit(node.right)
    elif node.op.type == TokenType.minus:
        return visit(node.left) - visit(node.right)
    elif node.op.type == TokenType.multiply:
        return visit(node.left) * visit(node.right)
    elif node.op.type == TokenType.divide:
        return visit(node.left) / visit(node.right)
