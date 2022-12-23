# -*- coding:utf-8 -*-

"""Monad Either representation tests."""

import pytest
from interpreter.either import make_left, make_right


def test_make_left():
    """Check that Either instance has the particular properties."""
    error_message = "Error message"
    either = make_left(error_message)
    assert either.is_left is True
    assert either.is_right is False
    assert either.get_left() == error_message


def test_make_right():
    """Check that Either instance has the particular properties."""
    value = 10
    either = make_right(value)
    assert either.is_right is True
    assert either.is_left is False
    assert either.get_right() == value


def test_make_left_exception():
    """Check that Either instance can throw exception."""
    with pytest.raises(RuntimeError):
        value = 10
        either = make_right(value)
        either.get_left()


def test_make_right_exception():
    """Check that Either instance can throw exception."""
    with pytest.raises(RuntimeError):
        error_message = "Error message"
        either = make_left(error_message)
        either.get_right()
