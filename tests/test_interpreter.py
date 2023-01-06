# -*- coding:utf-8 -*-

"""Interpreter representation tests."""

from itertools import permutations

import pytest
from interpreter.either import make_left, make_right
from interpreter.intereter import (
    apply_multiply_or_divide,
    apply_plus_or_minus,
    bind,
    is_token_plus_or_minus,
    try_get_integer,
)
from interpreter.lexer import get_tokens
from interpreter.token import Token, TokenType, make_eof, make_integer, make_sign


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
def test_apply_plus_or_minus1(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    result = apply_plus_or_minus(tokens)
    assert result.get_right().value == 21


@pytest.mark.parametrize(
    "test_input",
    ["10+11+11", "10 + 11 + 11 ", " 10 + 11   + 11"],
)
def test_apply_plus_or_minus2(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    result = apply_plus_or_minus(tokens)
    assert result.get_right().value == 32


@pytest.mark.parametrize(
    "test_input",
    ["10", "10 ", " 10 "],
)
def test_apply_plus_or_minus3(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    result = apply_plus_or_minus(tokens)
    assert result.get_right().value == 10


@pytest.mark.parametrize(
    "test_input",
    ["10-5", "10 - 5 ", " 10 - 5   "],
)
def test_apply_plus_or_minus4(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    result = apply_plus_or_minus(tokens)
    assert result.get_right().value == 5


@pytest.mark.parametrize(
    "test_input",
    ["10-5-2", "10 - 5 -2 ", " 10 - 5 - 2  "],
)
def test_apply_plus_or_minus5(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    result = apply_plus_or_minus(tokens)
    assert result.get_right().value == 3


@pytest.mark.parametrize(
    "test_input",
    ["10-5+2", "10 - 5 +2 ", " 10 - 5 + 2  "],
)
def test_apply_plus_or_minus6(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    result = apply_plus_or_minus(tokens)
    assert result.get_right().value == 7


@pytest.mark.parametrize(
    "test_input",
    ["10-2-5+2", "10 -2 - 5 +2 ", " 10-2 - 5 + 2  "],
)
def test_apply_plus_or_minus7(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    result = apply_plus_or_minus(tokens)
    assert result.get_right().value == 5


def test_get_integer_true():
    """Check a simple expression."""
    integers = [make_integer(10), make_integer(20)]
    either_integer = try_get_integer(iter(integers))
    assert either_integer.is_right is True
    assert either_integer.get_right().type == TokenType.integer
    assert either_integer.get_right().value == 10


def test_get_integer_false():
    """Check a simple expression."""
    integers = [
        make_sign("+"),
        make_sign("-"),
        make_sign("*"),
        make_sign("/"),
        make_eof(),
    ]
    iterator = iter(integers)
    count = 0
    while count < len(integers):
        either_integer = try_get_integer(iterator)
        assert either_integer.is_right is False
        assert either_integer.is_left is True

        count += 1


def test_get_integer_empty_list():
    """Check a simple expression."""
    empty = iter([])
    either_integer = try_get_integer(empty)
    assert either_integer.is_right is False
    assert either_integer.is_left is True


def test_bind_good():
    """Check a simple expression."""
    sign = make_sign("+")
    arg1 = make_right(make_integer(10))
    arg2 = make_right(make_integer(20))

    result = bind(func=sign, arg1=arg1, arg2=arg2)

    assert result.is_right is True
    assert result.get_right().value == 30


def test_bind_bad():
    """Check a simple expression."""
    tokens = (
        make_left(make_integer(10)),
        make_right(make_integer(20)),
    )

    func = (make_sign("+"),)
    for arg1, arg2 in permutations(tokens):
        result = bind(func, arg1, arg2)
        assert result.is_left is True


@pytest.mark.parametrize(
    "test_input",
    ["10-2-", "+10 -2", " 10 ++ 3  ", "-10++2++4"],
)
def test_apply_plus_or_minus_bad1(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    result = apply_plus_or_minus(tokens)
    assert result.is_left is True


@pytest.mark.parametrize(
    "test_input",
    ["10*11", "10 * 11 ", " 10 * 11 "],
)
def test_apply_multiply_or_divide1(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    result = apply_multiply_or_divide(tokens)
    assert result.get_right().value == 110


@pytest.mark.parametrize(
    "test_input",
    ["10/1", "10 / 1 ", " 10 / 1 "],
)
def test_apply_multiply_or_divide2(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    result = apply_multiply_or_divide(tokens)
    assert result.get_right().value == 10


@pytest.mark.parametrize(
    "test_input",
    ["10*2*5/2", "10 *2 * 5 /2 ", " 10*2 * 5 / 2  "],
)
def test_apply_multiply_or_divide3(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    result = apply_multiply_or_divide(tokens)
    assert result.get_right().value == 50


@pytest.mark.parametrize(
    "test_input",
    ["10*2*", "*10 /2", " 10 ** 3  ", "*10//2**4"],
)
def test_apply_multiply_or_divide_bad1(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    result = apply_multiply_or_divide(tokens)
    assert result.is_left is True
