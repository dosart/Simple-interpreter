# -*- coding:utf-8 -*-

import pytest

"""Users representation tests."""

from interpreter.either import *


def test_make_left():
    error_message = "Error message"
    either = make_left(error_message)
    assert either.is_left == True
    assert either.is_right == False
    assert either.get_left() == error_message


def test_make_right():
    value = 10
    either = make_right(value)
    assert either.is_right == True
    assert either.is_left == False
    assert either.get_right() == value


def test_make_left_exception():
    with pytest.raises(RuntimeError) as e_info:
        value = 10
        either = make_right(value)
        either.get_left()


def test_make_right_exception():
    with pytest.raises(RuntimeError) as e_info:
        error_message = "Error message"
        either = make_left(error_message)
        either.get_right()
