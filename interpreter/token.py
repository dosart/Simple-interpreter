# -*- coding:utf-8 -*-

"""Token's implementation. A token is an object that has a value and type."""

from enum import Enum


class TokenType(Enum):
    """Token's type implementation."""

    integer = (0,)
    plus = (1,)
    minus = (2,)
    multiply = (3,)
    divide = (4,)
    eof = (5,)
    error = (6,)
    lparen = (7,)
    rparen = (8,)
    dot = (9,)
    semi = (10,)
    assigin = (11,)
    begin = (12,)
    end = (13,)
    variable = (14,)
    program = (15,)
    var = (16,)
    integer_type = (17,)
    real_type = (18,)
    colon = (19,)
    comma = (20,)


class Token(object):
    """Token's implementation."""

    def __init__(self, token_type, token_value):
        """Construct a new either.

        Args:
            token_type: token type
            token_value: token value
        """
        self.value = token_value
        self.type = token_type

    def __str__(self):
        """Represent the class objects as a string.

        Returns:
            str: token as string
        """
        return "Token: type: {0}, value: {1}".format(self.type, self.value)


def make_single_symbols():
    """Return reserved interpreter symbols.

    Returns:
        dict: key(str), value(Token)
    """
    return {
        "+": Token(TokenType.plus, "+"),
        "-": Token(TokenType.minus, "-"),
        "*": Token(TokenType.multiply, "*"),
        "/": Token(TokenType.divide, "/"),
        "(": Token(TokenType.lparen, "("),
        ")": Token(TokenType.rparen, ")"),
        ".": Token(TokenType.dot, ","),
        ";": Token(TokenType.semi, ";"),
        ":=": Token(TokenType.assigin, ":="),
        ",": Token(TokenType.comma, ","),
    }


def make_keywords():
    """Return reserved interpreter symbols.

    Returns:
        dict: key(str), value(Token)
    """
    return {
        "BEGIN": Token(TokenType.begin, "BEGIN"),
        "END": Token(TokenType.end, "END"),
        "PROGRAM": Token(TokenType.program, "PROGRAM"),
        "VAR": Token(TokenType.program, "VAR"),
        "INTEGER": Token(TokenType.integer_type, "INTEGER_TYPE"),
        "REAL": Token(TokenType.real_type, "REAL_TYPE"),
    }


def make_keyword_token(keyword):
    """Return token for keyword.

    Args:
        keyword(str): reserved symbol sign

    Returns:
        token: an reserved symbol token or error token
    """
    keywords = make_keywords()
    return keywords.get(keyword, Token(TokenType.error, "?"))


def make_single_symbol_token(reserved_symbol):
    """Return token for reserved symbol.

    Args:
        reserved_symbol(str): reserved symbol sign

    Returns:
        token: an reserved symbol token or error token
    """
    symbols = make_single_symbols()
    return symbols.get(reserved_symbol, Token(TokenType.error, "?"))


def make_integer(token_value):
    """Return integer token.

    Args:
        token_value: token value

    Returns:
        token: an integer token
    """
    return Token(TokenType.integer, int(token_value))


def make_eof():
    """Return integer token.

    Returns:
        token: eof token
    """
    return Token(TokenType.eof, "")


def make_variable(variable_name):
    """Return variable token.

    Args:
        variable_name: variable name

    Returns:
        token: variable token
    """
    return Token(TokenType.variable, variable_name)
