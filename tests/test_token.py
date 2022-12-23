# -*- coding:utf-8 -*-

"""Token representation tests."""

from interpreter.token import TokenType, make_integer, make_plus


def test_make_integer():
    """Check that Either instance has the particular properties."""
    token_value = 10
    token = make_integer(token_value)
    assert token.value == token_value
    assert token.type == TokenType.integer


def test_make_plus():
    """Check that Either instance has the particular properties."""
    token_value = "+"
    token = make_plus(token_value)
    assert token.value == token_value
    assert token.type == TokenType.plus
