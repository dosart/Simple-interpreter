# -*- coding:utf-8 -*-

"""Implementing a Visitor template for AST."""

from functools import singledispatch

from interpreter.ast import (
    BinaryOperation,
    Num,
    UnaryOperation,
    CompoundOperator,
    AssiginOperator,
    Variable,
    EmptyOperator,
)
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
def __(node):
    """Visit Num node and return value.

    Args:
        node: integer

    Returns:
        value: calculation result
    """
    return node.value


@visit.register(BinaryOperation)
def __(node):
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
        if isinstance(node.right, Num) and node.right.value == 0:
            return 0
        return visit(node.left) / visit(node.right)


@visit.register(UnaryOperation)
def __(node):
    """Visit UnaryOperation node and return calculation result.

    Args:
        node: unary operation

    Returns:
        value: calculation result
    """
    if node.op.type == TokenType.plus:
        return +visit(node.expr)
    elif node.op.type == TokenType.minus:
        return -visit(node.expr)


@visit.register(CompoundOperator)
def __(node):
    """Visit CompoundOperator node and return calculation result.

    Args:
        node: compound operator
    """
    for child in node.compaund_statement:
        visit(child)


@visit.register(EmptyOperator)
def __(node):
    """Visit EmptyOperator and do nothing.

    Args:
        node: empty operator
    """
    pass


_GLOBAL_SCOPE = {}


@visit.register(AssiginOperator)
def __(node):
    """Visit assignment operator and save the value of the variable in the global scope.

    Args:
        node: empty operator
    """
    variable_name = node.left.value
    _GLOBAL_SCOPE[variable_name] = visit(node.right)
