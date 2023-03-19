# -*- coding:utf-8 -*-

"""Lexer representation tests."""

import pytest
from interpreter.lexer import get_tokens
from interpreter.token import (
    make_eof,
    make_integer,
    make_single_symbol_token,
    make_variable,
    make_keyword_token,
)


@pytest.mark.parametrize("test_input", ["", " ", "  "])
def test_empty_line(test_input):
    """Check a string consisting of whitespace does not form tokens.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    token = next(tokens)
    expected = make_eof()

    assert expected.type == token.type
    assert expected.value == token.value


@pytest.mark.parametrize("test_input", [";", " ;", ";  "])
def test_semi_token(test_input):
    """Check a string consisting of whitespace does not form tokens.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    token = next(tokens)
    expected = make_single_symbol_token(";")

    assert expected.type == token.type
    assert expected.value == token.value


@pytest.mark.parametrize("test_input", ["BEGIN", " BEGIN", "BEGIN  "])
def test_begin_token(test_input):
    """Check a string consisting of whitespace does not form tokens.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    token = next(tokens)
    expected = make_keyword_token("BEGIN")

    assert expected.type == token.type
    assert expected.value == token.value


@pytest.mark.parametrize("test_input", ["END", " END", "END  "])
def test_end_token(test_input):
    """Check a string consisting of whitespace does not form tokens.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    token = next(tokens)
    expected = make_keyword_token("END")

    assert expected.type == token.type
    assert expected.value == token.value


@pytest.mark.parametrize("test_input", ["a := 5 ", " a:=5 ", "  a :=  5   "])
def test_assign_token(test_input):
    """Check a string consisting of whitespace does not form tokens.

    Args:
        test_input: data for test
    """
    expected_values = (
        make_variable("a"),
        make_single_symbol_token(":="),
        make_integer(5),
    )
    for token, expected in zip(get_tokens(test_input), expected_values):
        assert token.type == expected.type
        assert token.value == expected.value


@pytest.mark.parametrize(
    "test_input", ["BEGIN a := 5  END", "BEGIN a:=5 END ", " BEGIN  a :=  5  END "]
)
def test_begin_assign_end_tokens1(test_input):
    """Check a string consisting of whitespace does not form tokens.

    Args:
        test_input: data for test
    """
    expected_values = (
        make_keyword_token("BEGIN"),
        make_variable("a"),
        make_single_symbol_token(":="),
        make_integer(5),
        make_keyword_token("END"),
    )
    for token, expected in zip(get_tokens(test_input), expected_values):
        assert token.type == expected.type
        assert token.value == expected.value


@pytest.mark.parametrize(
    "test_input",
    [
        "BEGIN a := 5; b := 11;  END",
        "BEGIN a:=5; b:=11; END ",
        " BEGIN  a :=  5; b:=11;  END ",
    ],
)
def test_begin_assign_end_tokens2(test_input):
    """Check a string consisting of whitespace does not form tokens.

    Args:
        test_input: data for test
    """
    expected_values = (
        make_keyword_token("BEGIN"),
        make_variable("a"),
        make_single_symbol_token(":="),
        make_integer(5),
        make_single_symbol_token(";"),
        make_variable("b"),
        make_single_symbol_token(":="),
        make_integer(11),
        make_single_symbol_token(";"),
        make_keyword_token("END"),
    )
    for token, expected in zip(get_tokens(test_input), expected_values):
        assert token.type == expected.type
        assert token.value == expected.value


@pytest.mark.parametrize("test_input", ["BEGIN BEGIN a := 5 END; b := 11;  END"])
def test_begin_assign_end_tokens3(test_input):
    """Check a string consisting of whitespace does not form tokens.

    Args:
        test_input: data for test
    """
    expected_values = (
        make_keyword_token("BEGIN"),
        make_keyword_token("BEGIN"),
        make_variable("a"),
        make_single_symbol_token(":="),
        make_integer(5),
        make_keyword_token("END"),
        make_single_symbol_token(";"),
        make_variable("b"),
        make_single_symbol_token(":="),
        make_integer(11),
        make_single_symbol_token(";"),
        make_keyword_token("END"),
    )
    for token, expected in zip(get_tokens(test_input), expected_values):
        assert token.type == expected.type
        assert token.value == expected.value


@pytest.mark.parametrize("test_input", ["BEGIN END .", " BEGIN END  ."])
def test_begin_assign_end_tokens4(test_input):
    """Check a string consisting of whitespace does not form tokens.

    Args:
        test_input: data for test
    """
    expected_values = (
        make_keyword_token("BEGIN"),
        make_keyword_token("END"),
        make_single_symbol_token("."),
    )
    for token, expected in zip(get_tokens(test_input), expected_values):
        assert token.type == expected.type
        assert token.value == expected.value


@pytest.mark.parametrize(
    "test_input", ["BEGIN x := 5 + 1 END .", " BEGIN x:=5+1 END  ."]
)
def test_begin_assign_end_tokens5(test_input):
    """Check a string consisting of whitespace does not form tokens.

    Args:
        test_input: data for test
    """
    expected_values = (
        make_keyword_token("BEGIN"),
        make_variable("x"),
        make_single_symbol_token(":="),
        make_integer(5),
        make_single_symbol_token("+"),
        make_integer(1),
        make_keyword_token("END"),
        make_single_symbol_token("."),
    )
    for token, expected in zip(get_tokens(test_input), expected_values):
        assert token.type == expected.type
        assert token.value == expected.value


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
        make_single_symbol_token("+"),
        make_integer(2),
    )
    for token, expected in zip(get_tokens(test_input), expected_values):
        assert token.type == expected.type
        assert token.value == expected.value


@pytest.mark.parametrize(
    "test_input",
    ["11+22", "11 + 22", " 11+ 22", " 11   +22", " 11 + 22 "],
)
def test_simple_expr2(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    expected_values = (
        make_integer(11),
        make_single_symbol_token("+"),
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
        make_single_symbol_token("-"),
        make_integer(2),
    )
    for token, expected in zip(get_tokens(test_input), expected_values):
        assert token.type == expected.type
        assert token.value == expected.value


@pytest.mark.parametrize(
    "test_input",
    ["11-22", "11 - 22", " 11- 22", " 11   -22", " 11 - 22 "],
)
def test_simple_expr4(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    expected_values = (
        make_integer(11),
        make_single_symbol_token("-"),
        make_integer(22),
    )
    for token, expected in zip(get_tokens(test_input), expected_values):
        assert token.type == expected.type
        assert token.value == expected.value


@pytest.mark.parametrize(
    "test_input",
    [
        "1-2 {comment}",
        "{comment} 1 - 2 ",
        "1 -{comment}2",
        "{comment}{comment} 1 {comment}-{comment}2{comment}",
    ],
)
def test_skip_comment1(test_input):
    """Check a simple expression.

    Args:
        test_input: data for test
    """
    expected_values = (
        make_integer(1),
        make_single_symbol_token("-"),
        make_integer(2),
    )
    for token, expected in zip(get_tokens(test_input), expected_values):
        assert token.type == expected.type
        assert token.value == expected.value


def test_skip_comment2():
    """Check a simple expression."""
    tokens1 = get_tokens("{comment}")
    tokens2 = get_tokens("{comment}{comments}")

    assert sum(0 for _ in tokens1) == 0
    assert sum(0 for _ in tokens2) == 0
