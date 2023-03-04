# -*- coding:utf-8 -*-

"""Token's implementation. A token is an object that has a value and type."""

from enum import Enum


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


def make_reserved_symbols():
    """Return reserved interpreter symbols.

    Returns:
        dict: key(str), value(Token)
    """
    return {
        "+": Token(TokenType.plus, "+"),
        "-": Token(TokenType.minus, "-"),
        "*": Token(TokenType.multiply, "*"),
        "/": Token(TokenType.divide, "/"),
        "(": Token(TokenType.lparen, "("),
        ")": Token(TokenType.rparen, ")"),
    }


def make_sign(sign):
    """Return integer token.

    Args:
        sign: token value

    Returns:
        token: an sign token
    """
    symbols = make_reserved_symbols()
    return symbols.get(sign, Token(TokenType.error, "?"))


def make_integer(token_value):
    """Return integer token.

    Args:
        token_value: token value

    Returns:
        token: an integer token
    """
    return Token(TokenType.integer, int(token_value))


def make_eof():
    """Return integer token.

    Returns:
        token: an eof token
    """
    return Token(TokenType.eof, "")
