# -*- coding:utf-8 -*-

"""Token's implementation. A token is an object that has a value and type."""

from enum import Enum
from operator import add, mul, sub, truediv


class TokenType(Enum):
    """Token's type implementation."""

    integer = (0,)
    plus = (1,)
    minus = (2,)
    multiply = (3,)
    divide = (4,)
    eof = (5,)
    error = (6,)
    lparen = (7,)
    rparen = 8


class Token(object):
    """Token's implementation."""

    def __init__(self, token_type, token_value):
        """Construct a new either.

        Args:
            token_type: token type
            token_value: token value
        """
        self.value = token_value
        self.type = token_type

    def __str__(self):
        """Represent the class objects as a string.

        Returns:
            str: token as string
        """
        return "Token: type: {0}, value: {1}".format(self.type, self.value)


_signs = {
    "+": Token(TokenType.plus, add),
    "-": Token(TokenType.minus, sub),
    "*": Token(TokenType.multiply, mul),
    "/": Token(TokenType.divide, truediv),
}


def make_sign(sign):
    """Return integer token.

    Args:
        sign: token value

    Returns:
        token: an sign token
    """
    return _signs.get(sign, Token(TokenType.error, "?"))


def make_integer(token_value):
    """Return integer token.

    Args:
        token_value: token value

    Returns:
        token: an integer token
    """
    return Token(TokenType.integer, token_value)


def make_eof():
    """Return integer token.

    Returns:
        token: an eof token
    """
    return Token(TokenType.eof, "")


def make_paren(paren):
    """Return paren token.

    Args:
        paren: token value

    Returns:
        token: an paren token
    """
    if paren == "(":
        return Token(TokenType.lparen, "(")
    if paren == ")":
        return Token(TokenType.rparen, ")")
    return Token(TokenType.error, "?")
