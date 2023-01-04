# -*- coding:utf-8 -*-

"""Interpreter's implementation."""


from interpreter.token import TokenType


def is_token_plus_or_minus(token):
    """Return true if the token is equal to plus or minus.

    Args:
        token: token for verification

    Returns:
        bool: true if the token is equal to plus or minus
    """
    return token.type in {TokenType.plus, token.type == TokenType.minus}
