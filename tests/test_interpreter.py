# -*- coding:utf-8 -*-

"""Interpreter representation tests."""

import pytest
from interpreter.intereter import apply, is_token_plus_or_minus
from interpreter.lexer import get_tokens
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


@pytest.mark.parametrize(
    "test_input",
    ["10+11", "10 + 11 ", " 10 + 11 "],
)
def test_apply1(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    result = apply(tokens)
    assert result.value == 21


@pytest.mark.parametrize(
    "test_input",
    ["10+11+11", "10 + 11 + 11 ", " 10 + 11   + 11"],
)
def test_apply2(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    result = apply(tokens)
    assert result.value == 32


@pytest.mark.parametrize(
    "test_input",
    ["10", "10 ", " 10 "],
)
def test_apply3(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    result = apply(tokens)
    assert result.value == 10


@pytest.mark.parametrize(
    "test_input",
    ["10-5", "10 - 5 ", " 10 - 5   "],
)
def test_apply4(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    result = apply(tokens)
    assert result.value == 5


@pytest.mark.parametrize(
    "test_input",
    ["10-5-2", "10 - 5 -2 ", " 10 - 5 - 2  "],
)
def test_apply5(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    result = apply(tokens)
    assert result.value == 3


@pytest.mark.parametrize(
    "test_input",
    ["10-5+2", "10 - 5 +2 ", " 10 - 5 + 2  "],
)
def test_apply6(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    result = apply(tokens)
    assert result.value == 7


@pytest.mark.parametrize(
    "test_input",
    ["10-2-5+2", "10 -2 - 5 +2 ", " 10-2 - 5 + 2  "],
)
def test_apply7(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    result = apply(tokens)
    assert result.value == 5
