# -*- coding:utf-8 -*-

"""Lexer's implementation. Simple lexer for large subset of Pascal language.

Can process simple arithmetic expressions of the type 3 + 5, 3 - 5, 11 + 5, 11 - 5
Work as a finite state machine. It has two states: a number and a sign.
"""


from itertools import takewhile

from interpreter.token import make_eof, make_integer, make_paren, make_sign


class TextIterator(object):
    """Implementing an iterator for a lexer."""

    def __init__(self, text):
        """Construct a new iterator.

        Args:
            text: program text
        """
        self.text = text
        self.current_char = None
        self.position = 0

    def __iter__(self):
        """Return an iterator object.

        Returns:
            iterator: an iterator object
        """
        return self

    def __next__(self):
        """Return the next item from the iterator.

        Raises:
            StopIteration: if there are no further item.

        Returns:
            item: yhe next item from the iterator
        """
        if self.position < len(self.text):
            self.current_char = self.text[self.position]
            self.position += 1
            return self.current_char
        raise StopIteration

    @property
    def current_item(self):
        """Return current iterator item.

        Returns:
            item: current iterator item
        """
        return self.current_char


def get_tokens(text):
    """Return tokens.

    Args:
        text: program text

    Returns:
        tokens: token iterator
    """
    tokens = []
    for token in get_token(text):
        tokens.append(token)
    return iter(tokens)


def get_token(text):
    """Return token generator.

    Args:
        text: program text

    Yields:
        tokens: token iterator
    """
    iterator = TextIterator(text)
    for char in iterator:
        if char.isspace():
            continue
        if char.isdigit():
            token = make_integer(_parse_integer(char, iterator))
            char = iterator.current_item
            yield token
        if char in {"+", "-", "*", "/"}:
            yield make_sign(char)
        if char in {"(", ")"}:
            yield make_paren(char)
    yield make_eof()


def _parse_integer(letter, text):
    digits = [letter]
    for digit in takewhile(lambda dig: dig.isdigit(), text):
        digits.append(digit)
    return int("".join(digits))
