# -*- coding:utf-8 -*-

"""Lexer's implementation. Simple lexer for large subset of Pascal language.

Can process simple arithmetic expressions of the type 3 + 5.
Work as a finite state machine. It has two states: a number and a sign.
"""

from interpreter.either import make_left, make_right
from interpreter.token import make_integer, make_plus


class Lexer(object):
    """Simple lexer's implementation."""

    def __init__(self):
        """Construct a new lexer."""
        # State machine transition function
        self._process_text = self._process_number

    def make_tokens(self, text):
        """Return list of tokens.

        Args:
            text: program text

        Returns:
            tokens: list of tokens
        """
        tokens = []

        for symbol in text:
            either_token = self._process_text(symbol)
            if is_token(either_token):
                tokens.append(get_token(either_token))

        return tokens

    def _process_number(self, symbol):
        if symbol.isdigit():
            self._process_text = self._process_sign
            return integer_either_token(symbol)
        return make_left("value isn't digit")

    def _process_sign(self, symbol):
        if symbol == "+":
            self._process_text = self._process_number
            return plus_either_token()
        return make_left("value isn't sign")


def is_token(either_token):
    """Check if the monad contains a value or an error.

    Args:
        either_token: eiter monad

    Returns:
        value: True if the monad contains value
    """
    return either_token.is_right


def get_token(either_token):
    """Return value from monad.

    Args:
        either_token: eiter monad

    Returns:
        value: value from monad
    """
    return either_token.get_right()


def plus_either_token():
    """Return token plus in either monad.

    Returns:
        either: token plus in either monad
    """
    return make_right(make_plus())


def integer_either_token(integer):
    """Return token integer in either monad.

    Args:
        integer: just integer

    Returns:
        integer: token integer in either monad
    """
    return make_right(make_integer(integer))
