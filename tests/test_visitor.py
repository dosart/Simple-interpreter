# -*- coding:utf-8 -*-

"""AST representation tests."""

import pytest
from interpreter.ast import (
    AssignOperator,
    BinaryOperation,
    CompoundOperator,
    EmptyOperator,
    Num,
    UnaryOperation,
    Variable,
)
from interpreter.lexer import get_token
from interpreter.token import make_integer, make_keyword_token, make_single_symbol_token
from interpreter.visitor import CalculationVisitor


def test_empty_operator():
    """Check a simple expression."""
    empty = EmptyOperator()

    visitor = CalculationVisitor(global_scope={})
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
    ast = _make_simple_arithmetic_expression(left, op, right)

    visitor = CalculationVisitor(global_scope={})
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
    first, op1, second, op2, third, result = test_input
    left_node = _make_simple_arithmetic_expression(first, op1, second)
    ast = BinaryOperation(
        left=left_node,
        op=make_single_symbol_token(op2),
        right=Num(make_integer(third)),
    )

    visitor = CalculationVisitor(global_scope={})
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

    visitor = CalculationVisitor(global_scope={})
    assert visitor.visit(ast) == result


def test_assign_operator_visitor():
    """Check a simple expression."""
    operator = _make_assign_operator("a:=5")
    global_scope = {}
    visitor = CalculationVisitor(global_scope)
    visitor.visit(operator)

    assert global_scope["a"] == 5


def test_compound_operator_visitor1():
    """Check a simple expression."""
    assign_operator = _make_assign_operator("a:=5")

    compound_operator = CompoundOperator()
    compound_operator.set_compound_statement([assign_operator])
    global_scope = {}
    visitor = CalculationVisitor(global_scope)
    visitor.visit(compound_operator)

    assert global_scope["a"] == 5


def test_compound_operator_visitor2():
    """Check a simple expression."""
    assign_operator1 = _make_assign_operator("a:=5")
    assign_operator2 = _make_assign_operator("b:=10")

    compound_operator = CompoundOperator()
    compound_operator.set_compound_statement([assign_operator1, assign_operator2])
    global_scope = {}
    visitor = CalculationVisitor(global_scope)
    visitor.visit(compound_operator)

    assert global_scope["a"] == 5
    assert global_scope["b"] == 10


def test_compound_operator_visitor3():
    """Check a simple expression."""
    assign_operator1 = _make_assign_operator("a:=5")
    assign_operator2 = _make_assign_operator("a:=10")

    compound_operator = CompoundOperator()
    compound_operator.set_compound_statement([assign_operator1, assign_operator2])
    global_scope = {}
    visitor = CalculationVisitor(global_scope)
    visitor.visit(compound_operator)

    assert global_scope["a"] == 10


def test_compound_operator_visitor4():
    """Check a simple expression."""
    compound_operator = CompoundOperator()
    compound_operator.set_compound_statement([])
    global_scope = {}
    visitor = CalculationVisitor(global_scope)
    visitor.visit(compound_operator)

    assert not global_scope


def test_unary_expression_visitor2():
    """Check a simple expression."""
    ast = BinaryOperation(
        left=Num(make_integer("5")),
        op=make_single_symbol_token("-"),
        right=_make_unary_expression("-", "2"),
    )
    visitor = CalculationVisitor(global_scope={})
    assert visitor.visit(ast) == 7


def _make_simple_arithmetic_expression(left, op, right):
    return BinaryOperation(
        Num(make_integer(left)),
        make_single_symbol_token(op),
        Num(make_integer(right)),
    )


def _make_unary_expression(op, expr):
    return UnaryOperation(
        op=make_single_symbol_token(op),
        expr=Num(make_integer(expr)),
    )


def _make_assign_operator(text):
    generator = get_token(text)

    return AssignOperator(
        variable=Variable(next(generator)),
        op=next(generator),
        expr=Num(next(generator)),
    )
