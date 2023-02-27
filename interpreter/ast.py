# -*- coding:utf-8 -*-

"""Abstract Syntax Tree's implementation."""


class AST(object):
    """Implementation of the AST base class."""

    pass


class Num(AST):
    """Implementation of the Int class."""

    def __init__(self, token):
        """Construct a new int object.

        Args:
            token: integer token
        """
        self.token = token
        self.value = token.value

    def __repr__(self):
        """Represent object as a string.

        Returns:
            str: represent object as a string

        """
        return "Num({value})".format(value=self.value)


class BinaryOperation(AST):
    """Implementation of the binary operator."""

    def __init__(self, left, op, right):
        """Construct a new binary operator.

        Args:
            left: integer token
            op: operator token
            right: integer token
        """
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        """Represent object as a string.

        Returns:
            str: represent object as a string

        """
        return "BinaryOperation({operator}, {left_child}, {right_child})".format(
            operator=self.op,
            left_child=self.left,
            right_child=self.right,
        )
