# -*- coding:utf-8 -*-

"""Lexer representation tests."""

import pytest
from interpreter.lexer import get_tokens
from interpreter.token import Token, TokenType, make_integer, make_sign, make_eof


@pytest.mark.parametrize("test_input", ["", " ", "  "])
def test_empty_line(test_input):
    """Check a string consisting of whitespace does not form tokens.

    Args:
        test_input: data for test
    """
    with pytest.raises(StopIteration):
        tokens = get_tokens(test_input)
        next(tokens)


@pytest.mark.parametrize("test_input", ["1", "1", "1", " 1", " 1 ", "   1   "])
def test_one_integer(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    token = next(tokens)
    expected = make_integer(1)

    assert expected.type == token.type
    assert expected.value == token.value


@pytest.mark.parametrize("test_input", ["1+2", "1 + 2", " 1+ 2", " 1   +2", " 1 + 2 "])
def test_simple_expr1(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    expected_values = (
        make_integer(1),
        make_sign("+"),
        make_integer(2),
    )
    for token, expected in zip(get_tokens(test_input), expected_values):
        assert token.type == expected.type
        assert token.value == expected.value


@pytest.mark.parametrize(
    "test_input", ["11+22", "11 + 22", " 11+ 22", " 11   +22", " 11 + 22 "]
)
def test_simple_expr2(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    expected_values = (
        make_integer(11),
        make_sign("+"),
        make_integer(22),
    )
    for token, expected in zip(get_tokens(test_input), expected_values):
        assert token.type == expected.type
        assert token.value == expected.value


@pytest.mark.parametrize("test_input", ["1-2", "1 - 2", " 1- 2", " 1   -2", " 1 - 2 "])
def test_simple_expr3(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    expected_values = (
        make_integer(1),
        make_sign("-"),
        make_integer(2),
    )
    for token, expected in zip(get_tokens(test_input), expected_values):
        assert token.type == expected.type
        assert token.value == expected.value


@pytest.mark.parametrize(
    "test_input", ["11-22", "11 - 22", " 11- 22", " 11   -22", " 11 - 22 "]
)
def test_simple_expr4(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    expected_values = (
        make_integer(11),
        make_sign("-"),
        make_integer(22),
    )
    for token, expected in zip(get_tokens(test_input), expected_values):
        assert token.type == expected.type
        assert token.value == expected.value
