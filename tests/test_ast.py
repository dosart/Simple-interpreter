# -*- coding:utf-8 -*-

"""AST representation tests."""

from interpreter.ast import BinaryOperation, Num, UnaryOperation
from interpreter.token import TokenType, make_integer, make_sign


def test_make_num():
    """Check a simple expression."""
    three_node = make_integer("3")
    node = Num(three_node)

    assert node.token is three_node
    assert node.value == 3


def test_make_simple_arithmetic_expression():
    """Check a simple expression."""
    mul_token = make_sign("*")
    plus_token = make_sign("+")

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
    minus_token = make_sign("-")

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
