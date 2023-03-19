# -*- coding:utf-8 -*-

"""Lexer's implementation. Simple lexer for large subset of Pascal language.

Can process simple arithmetic expressions of the type 3 + 5, 3 - 5, 11 + 5, 11 - 5
Work as a finite state machine. It has two states: a number and a sign.
"""


from itertools import takewhile

from interpreter.token import (
    make_eof,
    make_integer,
    make_keywords,
    make_single_symbol_token,
    make_single_symbols,
    make_variable,
)


class TextIterator(object):
    """Implementing an iterator for a lexer."""

    def __init__(self, text):
        """Construct a new iterator.

        Args:
            text: program text
        """
        self.text = text
        self.current_char = None
        self.previous_char = None
        self.next_char = None
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
            self.previous_char = self.current_char
            self.current_char = self.text[self.position]
            self.position += 1
            if self.position < len(self.text):
                self.next_char = self.text[self.position]
            else:
                self.next_char = None
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
    keywords = make_keywords()
    symbols = make_single_symbols()
    for char in iterator:
        if char.isspace():
            continue
        if char == "{":
            _skip_comment(iterator)
        if char.isalpha():
            word = _parse_word(char, iterator)
            char = iterator.current_item
            yield keywords.get(word, make_variable(word))
        if char.isdigit():
            token = make_integer(_parse_integer(char, iterator))
            char = iterator.current_item
            yield token
        if char == ":" and iterator.next_char == "=":
            next(iterator)
            yield make_single_symbol_token(":=")
        if char in symbols:
            yield symbols[char]
    yield make_eof()


def _skip_comment(text):
    for _ in takewhile(lambda char: char != "}", text):
        pass


def _parse_integer(letter, text):
    digits = [letter]
    for digit in takewhile(lambda dig: dig.isdigit(), text):
        digits.append(digit)
    return int("".join(digits))


def _parse_word(letter, text):
    word = [letter]
    for char in takewhile(lambda ch: ch.isalpha(), text):
        word.append(char)
    return "".join(word)
