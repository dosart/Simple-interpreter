# -*- coding:utf-8 -*-

"""AST representation tests."""

import pytest
from interpreter.ast import (
    AssiginOperator,
    BinaryOperation,
    CompoundOperator,
    EmptyOperator,
    Num,
    UnaryOperation,
    Variable,
)
from interpreter.lexer import get_token
from interpreter.token import make_integer, make_sign
from interpreter.visitor import CalculationVisitir


def test_empty_operator():
    """Check a simple expression."""
    empty = EmptyOperator()

    visitor = CalculationVisitir(global_scope={})
    assert visitor.visit(empty) is None


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
    """Check a simple expression.

    Args:
        test_input: data for tests
    """
    arguments, result = test_input
    left, op, right = arguments
    ast = _make_simple_arthmetic_exprassion(left, op, right)

    visitor = CalculationVisitir(global_scope={})
    assert visitor.visit(ast) == result


@pytest.mark.parametrize(
    "test_input",
    [(4, "*", 5, "+", 1, 21), (4, "*", 5, "-", 1, 19), (4, "/", 1, "+", 2, 6)],
)
def test_binary_expression_visitor2(test_input):
    """Check a simple expression.

    Args:
        test_input: data for tests
    """
    first, op1, secod, op2, third, result = test_input
    left_node = _make_simple_arthmetic_exprassion(first, op1, secod)
    ast = BinaryOperation(
        left=left_node,
        op=make_sign(op2),
        right=Num(make_integer(third)),
    )

    visitor = CalculationVisitir(global_scope={})
    assert visitor.visit(ast) == result


@pytest.mark.parametrize(
    "test_input",
    [("+", 1, 1), ("-", 5, -5), ("-", 0, 0), ("+", 0, 0)],
)
def test_unary_expression_visitor1(test_input):
    """Check a simple expression.

    Args:
        test_input: data for tests
    """
    op, expr, result = test_input
    ast = _make_unary_expression(op, expr)

    visitor = CalculationVisitir(global_scope={})
    assert visitor.visit(ast) == result


def test_assigin_operator_visitor():
    """Check a simple expression."""
    operator = _make_assigin_operator("a:=5")
    global_scope = {}
    visitor = CalculationVisitir(global_scope)
    visitor.visit(operator)

    assert global_scope["a"] == 5


def test_compaund_operator_visitor1():
    """Check a simple expression."""
    assigin_operator = _make_assigin_operator("a:=5")

    compound_operator = CompoundOperator()
    compound_operator.set_compound_statement([assigin_operator])
    global_scope = {}
    visitor = CalculationVisitir(global_scope)
    visitor.visit(compound_operator)

    assert global_scope["a"] == 5


def test_compaund_operator_visitor2():
    """Check a simple expression."""
    assigin_operator1 = _make_assigin_operator("a:=5")
    assigin_operator2 = _make_assigin_operator("b:=10")

    compound_operator = CompoundOperator()
    compound_operator.set_compound_statement([assigin_operator1, assigin_operator2])
    global_scope = {}
    visitor = CalculationVisitir(global_scope)
    visitor.visit(compound_operator)

    assert global_scope["a"] == 5
    assert global_scope["b"] == 10


def test_compaund_operator_visitor3():
    """Check a simple expression."""
    assigin_operator1 = _make_assigin_operator("a:=5")
    assigin_operator2 = _make_assigin_operator("a:=10")

    compound_operator = CompoundOperator()
    compound_operator.set_compound_statement([assigin_operator1, assigin_operator2])
    global_scope = {}
    visitor = CalculationVisitir(global_scope)
    visitor.visit(compound_operator)

    assert global_scope["a"] == 10


def test_compaund_operator_visitor4():
    """Check a simple expression."""
    compound_operator = CompoundOperator()
    compound_operator.set_compound_statement([])
    global_scope = {}
    visitor = CalculationVisitir(global_scope)
    visitor.visit(compound_operator)

    assert not global_scope


def test_unary_expression_visitor2():
    """Check a simple expression."""
    ast = BinaryOperation(
        left=Num(make_integer("5")),
        op=make_sign("-"),
        right=_make_unary_expression("-", "2"),
    )
    visitor = CalculationVisitir(global_scope={})
    assert visitor.visit(ast) == 7


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


def _make_assigin_operator(text):
    generator = get_token(text)

    return AssiginOperator(
        variable=Variable(next(generator)),
        op=next(generator),
        expr=Num(next(generator)),
    )
