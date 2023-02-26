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
            token(Token(TokenType.integer, token_value)): integer token
        """
        self.token = token
        self.value = token.value

    def __repr__(self):
        return "Num(%d)" % self.value


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
        return "BinaryOperation(%s, %s, %s)" % (self.op, self.left, self.right)
