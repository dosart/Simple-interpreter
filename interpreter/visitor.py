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


class CalculationVisitir(object):
    def __init__(self):
        self._global_scope = {}

    def calculate(self, node):
        methods = {
            Num: self._calculate_num,
            BinaryOperation: self._calculate_binary_operation,
            UnaryOperation: self._calculate_unary_operation,
            CompoundOperator: self._calculate_compaund_operator,
            EmptyOperator: self._calculate_empty_operator,
            AssiginOperator: self._calculate_assigin_operator,
            Variable: self._calculate_variable,
        }
        method = methods.get(type(node), self._error)
        method(node)

    def _calculate_num(self, node):
        """Visit Num node and return value.

        Args:
            node: integer

        Returns:
            value: calculation result
        """

    return node.value

    def _calculate_binary_operation(self, node):
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

    def _calculate_unary_operation(self, node):
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

    def _calculate_compaund_operator(self, node):
        """Visit CompoundOperator node and return calculation result.

        Args:
            node: compound operator
        """
        for statement in node.compaund_statement:
            visit(statement)

    def _calculate_empty_operator():
        pass

    def _calculate_assigin_operator(self, node):
        """Visit assignment operator and save the value of the variable in the global scope.

        Args:
            node: empty operator
        """
        variable_name = node.left.value
        self._global_scope[variable_name] = visit(node.right)

    def _calculate_variable(self, node):
        """Visit variable and return value.

        Args:
            node: variable

        Returns:
            value: value of variable
        """
        var_name = node.value
        val = self._global_scope.get(var_name, None)
        if val is None:
            raise NameError(repr(var_name))
        else:
            return val

    def _error(self, node):
        """Raise error.
        Args:
            node: unknown type
        Raises:
            AttributeError: raise exception
        """
        type_name = type(node)
        raise AttributeError(
            "No handler found for {type_name}".format(type_name=type_name)
        )
