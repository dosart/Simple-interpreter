# -*- coding:utf-8 -*-

"""Lexer representation tests."""

import pytest
from interpreter.lexer import get_tokens, _parse_number, _parse_word, TextIterator
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


@pytest.mark.parametrize("test_input", ["PROGRAM" " PROGRAM", "PROGRAM  "])
def test_program_token1(test_input):
    """Check a string consisting of whitespace does not form tokens.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    token = next(tokens)
    expected = make_keyword_token("PROGRAM")

    assert expected.type == token.type
    assert expected.value == token.value


@pytest.mark.parametrize("test_input", ["PROGRAM v1;" " PROGRAM v1 ;", "PROGRAM v1 ; "])
def test_program_token1(test_input):
    """Check a string consisting of whitespace does not form tokens.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    program_token = next(tokens)
    variable_token = next(tokens)
    semi_token = next(tokens)

    expected_program = make_keyword_token("PROGRAM")
    expected_variable = make_variable("v1")
    expected_semi = make_single_symbol_token(";")

    assert expected_program.type == program_token.type
    assert expected_program.value == program_token.value

    assert expected_variable.type == variable_token.type
    assert expected_variable.value == variable_token.value

    assert expected_semi.type == semi_token.type
    assert expected_semi.value == semi_token.value


@pytest.mark.parametrize(
    "test_input",
    [
        "PROGRAM v1; VAR x:INTEGER",
        " PROGRAM v1 ; VAR x : INTEGER",
        "PROGRAM v1 ;\n VAR x : INTEGER",
    ],
)
def test_program_token2(test_input):
    """Check a string consisting of whitespace does not form tokens.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    program_token = next(tokens)
    variable_token1 = next(tokens)
    semi_token = next(tokens)
    var_token = next(tokens)
    variable_token2 = next(tokens)
    colon_token = next(tokens)
    integer_token = next(tokens)

    expected_program = make_keyword_token("PROGRAM")
    expected_variable1 = make_variable("v1")
    expected_semi = make_single_symbol_token(";")
    expected_var = make_keyword_token("VAR")
    expected_variable2 = make_variable("x")
    expected_colon = make_single_symbol_token(":")
    expected_integer = make_keyword_token("INTEGER")

    assert expected_program.type == program_token.type
    assert expected_program.value == program_token.value

    assert expected_variable1.type == variable_token1.type
    assert expected_variable1.value == variable_token1.value

    assert expected_semi.type == semi_token.type
    assert expected_semi.value == semi_token.value

    assert expected_var.type == var_token.type
    assert expected_var.value == var_token.value

    assert expected_variable2.type == variable_token2.type
    assert expected_variable2.value == variable_token2.value

    assert expected_colon.type == colon_token.type
    assert expected_colon.value == colon_token.value

    assert expected_integer.type == integer_token.type
    assert expected_integer.value == integer_token.value


@pytest.mark.parametrize(
    "test_input",
    [
        "PROGRAM program; VAR x:REAL",
        " PROGRAM program ; VAR x : REAL",
        "PROGRAM program ;\n VAR x : REAL",
    ],
)
def test_program_token3(test_input):
    """Check a string consisting of whitespace does not form tokens.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    program_token = next(tokens)
    variable_token1 = next(tokens)
    semi_token = next(tokens)
    var_token = next(tokens)
    variable_token2 = next(tokens)
    colon_token = next(tokens)
    integer_token = next(tokens)

    expected_program = make_keyword_token("PROGRAM")
    expected_variable1 = make_variable("program")
    expected_semi = make_single_symbol_token(";")
    expected_var = make_keyword_token("VAR")
    expected_variable2 = make_variable("x")
    expected_colon = make_single_symbol_token(":")
    expected_integer = make_keyword_token("REAL")

    assert expected_program.type == program_token.type
    assert expected_program.value == program_token.value

    assert expected_variable1.type == variable_token1.type
    assert expected_variable1.value == variable_token1.value

    assert expected_semi.type == semi_token.type
    assert expected_semi.value == semi_token.value

    assert expected_var.type == var_token.type
    assert expected_var.value == var_token.value

    assert expected_variable2.type == variable_token2.type
    assert expected_variable2.value == variable_token2.value

    assert expected_colon.type == colon_token.type
    assert expected_colon.value == colon_token.value

    assert expected_integer.type == integer_token.type
    assert expected_integer.value == integer_token.value


@pytest.mark.parametrize(
    "test_input",
    [
        "PROGRAM program; VAR x:REAL; y:INTEGER;",
        " PROGRAM program ; VAR x : REAL; y:INTEGER;",
        "PROGRAM program ;\n VAR x : REAL; y : INTEGER;",
    ],
)
def test_program_token4(test_input):
    """Check a string consisting of whitespace does not form tokens.

    Args:
        test_input: data for test
    """
    tokens = get_tokens(test_input)
    program_token = next(tokens)
    variable_token1 = next(tokens)
    semi_token1 = next(tokens)
    var_token = next(tokens)
    variable_token2 = next(tokens)
    colon_token = next(tokens)
    real_token = next(tokens)
    semi_token2 = next(tokens)
    variable_token3 = next(tokens)
    colon_token2 = next(tokens)
    integer_token = next(tokens)
    semi_token3 = next(tokens)

    expected_program = make_keyword_token("PROGRAM")
    expected_variable1 = make_variable("program")
    expected_semi1 = make_single_symbol_token(";")
    expected_var = make_keyword_token("VAR")
    expected_variable2 = make_variable("x")
    expected_colon = make_single_symbol_token(":")
    expected_real = make_keyword_token("REAL")
    expected_semi2 = make_single_symbol_token(";")
    expected_variable3 = make_variable("y")
    expected_colon2 = make_single_symbol_token(":")
    expected_integer = make_keyword_token("INTEGER")
    expected_semi3 = make_single_symbol_token(";")

    assert expected_program.type == program_token.type
    assert expected_program.value == program_token.value

    assert expected_variable1.type == variable_token1.type
    assert expected_variable1.value == variable_token1.value

    assert expected_semi1.type == semi_token1.type
    assert expected_semi1.value == semi_token1.value

    assert expected_var.type == var_token.type
    assert expected_var.value == var_token.value

    assert expected_variable2.type == variable_token2.type
    assert expected_variable2.value == variable_token2.value

    assert expected_colon.type == colon_token.type
    assert expected_colon.value == colon_token.value

    assert expected_real.type == real_token.type
    assert expected_real.value == real_token.value

    assert expected_semi2.type == semi_token2.type
    assert expected_semi2.value == semi_token2.value

    assert expected_variable3.type == variable_token3.type
    assert expected_variable3.value == variable_token3.value

    assert expected_colon2.type == colon_token2.type
    assert expected_colon2.value == colon_token2.value

    assert expected_integer.type == integer_token.type
    assert expected_integer.value == integer_token.value

    assert expected_semi3.type == semi_token3.type
    assert expected_semi3.value == semi_token3.value


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


def test_parse_int_number():
    """Check a simple expression."""
    assert _run_parse(_parse_number, "0") == 0
    assert _run_parse(_parse_number, "1") == 1
    assert _run_parse(_parse_number, "22") == 22
    assert _run_parse(_parse_number, "100") == 100


def test_parse_float_number():
    """Check a simple expression."""
    assert _run_parse(_parse_number, "0.1") == 0.1
    assert _run_parse(_parse_number, "0.15") == 0.15
    assert _run_parse(_parse_number, "0.155") == 0.155

    assert _run_parse(_parse_number, "1.0") == 1.0
    assert _run_parse(_parse_number, "22.5") == 22.5
    assert _run_parse(_parse_number, "100.10") == 100.10


def test_parse_word():
    """Check a simple expression."""
    assert _run_parse(_parse_word, "hello") == "hello"
    assert _run_parse(_parse_word, "hEllo") == "hEllo"
    assert _run_parse(_parse_word, "hello   ") == "hello"
    assert _run_parse(_parse_word, "hello:") == "hello"
    assert _run_parse(_parse_word, "hello:=") == "hello"


def _run_parse(parse_function, text):
    first = text[0]
    new_text = text[1:]
    iterator = TextIterator(new_text)

    return parse_function(first, iterator)
