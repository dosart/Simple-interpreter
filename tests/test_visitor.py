# -*- coding:utf-8 -*-

"""AST representation tests."""

import pytest
from interpreter.ast import BinaryOperation, Num, UnaryOperation
from interpreter.token import TokenType, make_integer, make_sign
from interpreter.visitor import visit


@pytest.mark.parametrize(
    "test_input",
    [
        ((4, "+", 5), 9),
        ((4, "*", 5), 20),
        ((4, "-", 5), -1),
        ((20, "/", 4), 5),
        ((20, "/", 0), 0),
    ],
)
def test_binary_expression_visitor1(test_input):
    """Check a simple expression."""
    arguments, result = test_input
    left, op, right = arguments
    ast = _make_simple_arthmetic_exprassion(left, op, right)

    assert visit(ast) == result


@pytest.mark.parametrize(
    "test_input",
    [(4, "*", 5, "+", 1, 21), (4, "*", 5, "-", 1, 19), (4, "/", 1, "+", 2, 6)],
)
def test_binary_expression_visitor2(test_input):
    """Check a simple expression."""
    first, op1, secod, op2, third, result = test_input
    left_node = _make_simple_arthmetic_exprassion(first, op1, secod)
    ast = BinaryOperation(
        left=left_node, op=make_sign(op2), right=Num(make_integer(third))
    )

    assert visit(ast) == result


@pytest.mark.parametrize(
    "test_input",
    [("+", 1, 1), ("-", 5, -5), ("-", 0, 0), ("+", 0, 0)],
)
def test_unary_expression_visitor1(test_input):
    """Check a simple expression."""
    op, expr, result = test_input
    ast = _make_unary_expression(op, expr)

    assert visit(ast) == result


def test_unary_expression_visitor2():
    ast = BinaryOperation(
        left=Num(make_integer("5")),
        op=make_sign("-"),
        right=_make_unary_expression("-", "2"),
    )
    assert visit(ast) == 7


def _make_simple_arthmetic_exprassion(left, op, right):
    return BinaryOperation(
        Num(make_integer(left)),
        make_sign(op),
        Num(make_integer(right)),
    )


def _make_unary_expression(op, expr):
    return UnaryOperation(
        op=make_sign(op),
        expr=Num(make_integer(expr)),
    )
