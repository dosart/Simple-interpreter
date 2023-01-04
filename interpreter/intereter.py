# -*- coding:utf-8 -*-

"""Interpreter's implementation."""

from itertools import takewhile

from interpreter.token import TokenType


def is_token_plus_or_minus(token):
    """Return true if the token is equal to plus or minus.

    Args:
        token: token for verification

    Returns:
        bool: true if the token is equal to plus or minus
    """
    return token.type in {TokenType.plus, TokenType.minus}


def apply(tokens):
    """Calculate simple arithmetic expressions (+ and -sign only).

    Args:
        tokens: the expression consists of tokens

    Returns:
        int: the result of calculating the expression
    """
    result = next(tokens)
    for sign in takewhile(is_token_plus_or_minus, tokens):
        right = next(tokens)
        result.value = sign.value(result.value, right.value)
    return result
