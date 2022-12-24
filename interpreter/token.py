# -*- coding:utf-8 -*-

"""Token's implementation. A token is an object that has a value and type."""

from enum import Enum


class TokenType(Enum):
    """Token's type implementation."""

    integer = 0
    plus = 1


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


def make_integer(token_value):
    """Return integer token.

    Args:
        token_value: token value

    Returns:
        token: an integer token
    """
    return Token(TokenType.integer, token_value)


def make_plus():
    """Return plus token.

    Returns:
        token: an plus token
    """
    return Token(TokenType.plus, "+")
