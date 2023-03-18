# -*- coding:utf-8 -*-

"""AST representation tests."""

from interpreter.ast import (
    BinaryOperation,
    Num,
    UnaryOperation,
    AssignOperator,
    Variable,
    CompoundOperator,
)
from interpreter.token import (
    TokenType,
    make_integer,
    make_reserved_symbol_token,
    make_variable,
    make_reserved_symbol_token,
)


def test_make_num():
    """Check a simple expression."""
    three_node = make_integer("3")
    node = Num(three_node)

    assert node.token is three_node
    assert node.value == 3


def test_make_simple_arithmetic_expression():
    """Check a simple expression."""
    mul_token = make_reserved_symbol_token("*")
    plus_token = make_reserved_symbol_token("+")

    three_node = make_integer("3")
    two_node = make_integer("2")
    seven_node = make_integer("7")

    mul_node = BinaryOperation(
        left=Num(three_node),
        op=mul_token,
        right=Num(seven_node),
    )
    plus_node = BinaryOperation(left=Num(two_node), op=plus_token, right=mul_node)

    assert mul_node.left.token.type == TokenType.integer
    assert mul_node.op.type == TokenType.multiply
    assert mul_node.right.token.type == TokenType.integer

    assert mul_node.left.token.value == 3
    assert mul_node.right.token.value == 7

    assert plus_node.left.token.type == TokenType.integer
    assert plus_node.op.type == TokenType.plus

    assert plus_node.left.token.value == 2
    assert plus_node.right is mul_node


def test_make_unary_operation():
    """Check a simple expression."""
    minus_token = make_reserved_symbol_token("-")

    three_node = make_integer("3")
    two_node = make_integer("2")

    expr_node = BinaryOperation(
        Num(three_node),
        minus_token,
        UnaryOperation(minus_token, UnaryOperation(minus_token, Num(two_node))),
    )

    assert expr_node.op is minus_token
    assert expr_node.op.type == TokenType.minus

    assert expr_node.right.op is minus_token
    assert expr_node.right.expr.op is minus_token
    assert expr_node.right.expr.expr.value == 2


def test_make_variable():
    """Check a simple expression."""
    variable_token = make_variable("a")
    variable_node = Variable(variable_token)

    assert variable_node.value == "a"


def test_str():
    """Check a simple expression."""
    three_token = make_integer("3")
    two_token = make_integer("2")
    plus_token = make_reserved_symbol_token("+")
    variable_token = make_variable("a")
    assign_token = make_reserved_symbol_token(":=")

    three_node = Num(three_token)
    two_node = Num(two_token)
    binary_operation_node = BinaryOperation(
        left=three_node, op=plus_token, right=two_node
    )

    unary_operation_node = UnaryOperation(plus_token, three_node)
    variable_node = Variable(variable_token)
    assign_operator_node = AssignOperator(
        variable_node, assign_token, binary_operation_node
    )

    compound_operator_node = CompoundOperator()
    compound_operator_node.add_statement(assign_operator_node)
    compound_operator_node.add_statement(unary_operation_node)

    assert str(three_node) == "Num(3)"
    assert str(two_node) == "Num(2)"
    assert str(binary_operation_node) == "BinaryOperation(Num(3) + Num(2))"
    assert str(unary_operation_node) == "UnaryOperation(+ Num(3))"
    assert str(variable_node) == "Variable(a)"
    assert (
        str(assign_operator_node)
        == "AssignOperator(Variable(a) := BinaryOperation(Num(3) + Num(2)))"
    )
    assert (
        str(compound_operator_node)
        == "CompoundOperator(BEGIN AssignOperator(Variable(a) := BinaryOperation(Num(3) + Num(2))) UnaryOperation(+ Num(3)) END)"
    )
