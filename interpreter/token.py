# -*- coding:utf-8 -*-

"""Token's implementation. A token is an object that has a value and type."""

from enum import Enum


class TokenType(Enum):
    """Token's type implementation."""

    integer = 0
    plus = (1,)
    minus = (2,)
    multiply = (3,)
    divide = (4,)
    eof = (5,)
    error = 6


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
    "+": Token(TokenType.plus, "+"),
    "-": Token(TokenType.minus, "-"),
    "*": Token(TokenType.multiply, "*"),
    "/": Token(TokenType.divide, "/"),
}


def make_sign(sign):
    return _signs.get(sign, Token(TokenType.error, "?"))


def make_integer(value):
    return Token(TokenType.integer, value)


def make_eof():
    return Token(TokenType.eof, "")
