# -*- coding:utf-8 -*-

"""Lexer representation tests."""

import pytest
from interpreter.either import make_left
from interpreter.lexer import Lexer, integer_either_token, is_token, plus_either_token
from interpreter.token import make_integer, make_plus


def test_is_token_plus():
    """Сheck the possibility of creating a plus token."""
    assert is_token(plus_either_token()) is True


@pytest.mark.parametrize("test_input", ["+", "-", "*", "/"])
def test_only_sign(test_input):
    """Check a string consisting of a single sign does not form tokens.

    Args:
        test_input: data for test
    """
    lexer = Lexer()
    tokens = lexer.make_tokens(test_input)

    assert not tokens


@pytest.mark.parametrize("test_input", [" + ", " -", " *", " /", " - ", " *  ", " / "])
def test_sign_with_whitespace(test_input):
    """Check a string consisting of a sign does not form tokens.

    Args:
        test_input: data for test
    """
    lexer = Lexer()
    tokens = lexer.make_tokens(test_input)

    assert not tokens


@pytest.mark.parametrize("test_input", ["", " ", "  "])
def test_empty_line(test_input):
    """Check a string consisting of whitespace does not form tokens.

    Args:
        test_input: data for test
    """
    lexer = Lexer()
    tokens = lexer.make_tokens(test_input)

    assert not tokens


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (make_left, False),
        (integer_either_token, True),
    ],
)
def test_is_token(test_input, expected):
    """Check the possibility of creating a token by factories.

    Args:
        test_input: data for test
        expected: reference data
    """
    assert is_token(test_input(10)) is expected


@pytest.mark.parametrize("test_input", ["1", "1", "1", " 1", " 1 ", "   1   "])
def test_one_integer(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    lexer = Lexer()
    tokens = lexer.make_tokens(test_input)
    expected = make_integer("1")
    token = tokens[0]

    assert len(tokens) == 1
    assert expected.type == token.type
    assert expected.value == token.value


@pytest.mark.parametrize("test_input", ["1+2", "1 + 2", " 1+ 2", " 1   +2", " 1 + 2 "])
def test_simple_expr(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    lexer = Lexer()
    tokens = lexer.make_tokens(test_input)
    expected_values = (make_integer("1"), make_plus(), make_integer("2"))

    assert len(tokens) == 3
    for token, expected in zip(tokens, expected_values):
        assert token.type == expected.type
        assert token.value == expected.value
