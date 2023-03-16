# -*- coding:utf-8 -*-

"""Implementing a Visitor template for AST."""


from interpreter.ast import (
    AssignOperator,
    BinaryOperation,
    CompoundOperator,
    EmptyOperator,
    Num,
    UnaryOperation,
    Variable,
)
from interpreter.token import TokenType


class CalculationVisitor(object):
    """Represent a visitor to bypass the AST and visit the result."""

    def __init__(self, global_scope):
        """Construct a new visitor.

        Args:
            global_scope (dict): global scope for storing variables
        """
        self._global_scope = global_scope

    def visit(self, node):
        """Visit all nodes in AST.

        Args:
            node: node to run

        Returns:
            result: calculation result (tree traversal result)
        """
        methods = {
            Num: self._visit_num,
            BinaryOperation: self._visit_binary_operation,
            UnaryOperation: self._visit_unary_operation,
            CompoundOperator: self._visit_compaund_operator,
            EmptyOperator: self._visit_empty_operator,
            AssignOperator: self._visit_assigin_operator,
            Variable: self._visit_variable,
        }
        method = methods.get(type(node), self._error)
        return method(node)

    def _visit_num(self, node):
        """Visit Num node and return value.

        Args:
            node: integer

        Returns:
            value: calculation result
        """
        return node.value

    def _visit_binary_operation(self, node):
        """Visit BinaryOperation node and return calculation result.

        Args:
            node: bynary operation

        Returns:
            value: calculation result
        """
        if node.op.type == TokenType.plus:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == TokenType.minus:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == TokenType.multiply:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == TokenType.divide:
            if isinstance(node.right, Num) and node.right.value == 0:
                return 0
        return self.visit(node.left) / self.visit(node.right)

    def _visit_unary_operation(self, node):
        """Visit UnaryOperation node and return calculation result.

        Args:
            node: unary operation

        Returns:
            value: calculation result
        """
        if node.op.type == TokenType.plus:
            return +self.visit(node.expr)
        elif node.op.type == TokenType.minus:
            return -self.visit(node.expr)

    def _visit_compaund_operator(self, node):
        """Visit CompoundOperator node and return calculation result.

        Args:
            node: compound operator
        """
        for statement in node.compound_statement:
            self.visit(statement)

    def _visit_empty_operator(self, node):
        pass

    def _visit_assigin_operator(self, node):
        """Visit assignment operator and save the value of the variable in the global scope.

        Args:
            node: empty operator
        """
        variable_name = node.variable.value
        self._global_scope[variable_name] = self.visit(node.expr)

    def _visit_variable(self, node):
        """Visit variable and return value.

        Args:
            node: variable

        Raises:
             NameError: if the variable is not in scope

        Returns:
            value: value of variable
        """
        var_name = node.value
        val = self._global_scope.get(var_name, None)
        if val is None:
            raise NameError(repr(var_name))
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
            "No handler found for {type_name}".format(type_name=type_name),
        )
