# -*- coding:utf-8 -*-

"""Leer's implementation. Simple lexer for large subset of Pascal language.

Can process simple arithmetic expressions of the type 3 + 5, 3 - 5, 11 + 5, 11 - 5
Work as a finite state machine. It has two states: a number and a sign.
"""

from interpreter.either import make_left, make_right
from interpreter.token import Token, TokenType, make_sign, make_integer, make_eof
from itertools import takewhile


class TextIterator(object):
    def __init__(self, text):
        self.text = text
        self.current_char = None
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < len(self.text):
            self.current_char = self.text[self.position]
            self.position += 1
            return self.current_char
        raise StopIteration

    def get_current_char(self):
        return self.current_char


def get_tokens(text):
    tokens = []
    for token in get_token(text):
        tokens.append(token)
    return iter(tokens)


def get_token(text):
    iterator = TextIterator(text)
    for char in iterator:
        if char.isspace():
            continue
        if char.isdigit():
            token = make_integer(parse_integer(char, iterator))
            char = iterator.get_current_char()
            yield token
        if char == "+":
            yield make_sign("+")
        if char == "-":
            yield make_sign("-")
    return make_eof()


def parse_integer(letter, text):
    result = letter
    for digit in takewhile(lambda d: d.isdigit(), text):
        result += digit
    return int(result)
