# -*- coding:utf-8 -*-

"""Lexer representation tests."""

import pytest
from interpreter.intereter import is_token_plus_or_minus
from interpreter.token import Token, TokenType


@pytest.mark.parametrize(
    "test_input",
    [TokenType.integer, TokenType.eof, TokenType.multiply, TokenType.divide],
)
def test_is_token_plus_or_minus1(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    token = Token(test_input, 0)
    assert is_token_plus_or_minus(token) is False


@pytest.mark.parametrize(
    "test_input",
    [TokenType.plus, TokenType.minus],
)
def test_is_token_plus_or_minus2(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    token = Token(test_input, 0)
    assert is_token_plus_or_minus(token) is True
