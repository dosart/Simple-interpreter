# -*- coding:utf-8 -*-

"""Interpreter's implementation."""

from itertools import takewhile

from interpreter.either import make_error_message, make_left, make_right
from interpreter.token import TokenType, make_integer


def apply_plus_or_minus(tokens):
    """Calculate simple arithmetic expressions (+ and - sign only).

    Args:
        tokens: the expression consists of tokens

    Returns:
        int: the result of calculating the expression
    """
    return apply(tokens, is_token_plus_or_minus)


def apply_multiply_or_divide(tokens):
    """Calculate simple arithmetic expressions (* and / sign only).

    Args:
        tokens: the expression consists of tokens

    Returns:
        int: the result of calculating the expression
    """
    return apply(tokens, is_token_multiply_or_divide)


def is_token_plus_or_minus(token):
    """Return true if the token is equal to plus or minus.

    Args:
        token: token for verification

    Returns:
        bool: true if the token is equal to plus or minus
    """
    return token.type in {TokenType.plus, TokenType.minus}


def is_token_multiply_or_divide(token):
    """Return true if the token is equal to multiply or divide.

    Args:
        token: token for verification

    Returns:
        bool: true if the token is equal to multiply or divide
    """
    return token.type in {TokenType.multiply, TokenType.divide}


def apply(tokens, predicate):
    """Calculate simple arithmetic expressions.

    Args:
        tokens: the expression consists of tokens
        predicate: which tokens need to be returned

    Returns:
        int: the result of calculating the expression
    """
    result = try_get_integer(tokens)
    for sign in takewhile(predicate, tokens):
        right = try_get_integer(tokens)
        result = bind(sign, result, right)
    return result


def try_get_integer(iterator):
    """Return the current taken from the iterator to the monad either.

    Args:
        iterator: iterator containing tokens

    Returns:
        either: monad contains token. if the type is not an integer return left
    """
    try:
        return get_token(iterator, {TokenType.integer})
    except StopIteration:
        return make_left(make_error_message("value isn't integer"))


def try_get_sign(iterator):
    """Return the current taken from the iterator to the monad either.

    Args:
        iterator: iterator containing tokens

    Returns:
        either: monad contains token. if the type is not a sign return left
    """
    try:
        return get_token(iterator, {TokenType.plus, TokenType.minus})
    except StopIteration:
        return make_left(make_error_message("value isn't sign"))


def get_token(iterator, token_types):
    """Return the current token from the iterator. Check the current token type.

    Args:
        iterator: iterator containing tokens
        token_types(set): if the type is not a token_types return left

    Returns:
        either: monad contains tokens
    """
    maybe_integer = next(iterator)
    if maybe_integer.type in token_types:
        return make_right(maybe_integer)
    return make_left("value isn't correct")


def bind(func, arg1, arg2):
    """Return the result of func(arg1, arg2).

    Args:
        func: function
        arg1: argument of a function in either monad
        arg2: argument of a function in either monad

    Returns:
        either: the monad contains the result tokens func(arg1, arg2)
    """
    if arg1.is_left:
        return arg1
    if arg2.is_left:
        return arg2

    one = arg1.get_right()
    two = arg2.get_right()

    result = make_integer(0)
    result.value = func.value(one.value, two.value)
    return make_right(result)
