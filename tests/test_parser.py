# # -*- coding:utf-8 -*-

# """Interpreter representation tests."""


from interpreter.lexer import get_token
from interpreter.parser import Parser
from interpreter.visitor import CalculationVisitor


def test_apply_plus():
    """Test a private method."""
    parser = Parser(get_token("10+11+11"))
    ast = parser._expr()
    visitor = CalculationVisitor(global_scope={})

    assert visitor.visit(ast) == 32


def test_apply_single_number():
    """Test a private method."""
    parser = Parser(get_token("10"))
    ast = parser._expr()
    visitor = CalculationVisitor(global_scope={})

    assert visitor.visit(ast) == 10


def test_apply_minus1():
    """Check a simple expression."""
    parser = Parser(get_token("10-5"))
    ast = parser._expr()
    visitor = CalculationVisitor(global_scope={})

    assert visitor.visit(ast) == 5


def test_apply_minus2():
    """Check a simple expression."""
    parser = Parser(get_token("10-5-2"))
    ast = parser._expr()
    visitor = CalculationVisitor(global_scope={})

    assert visitor.visit(ast) == 3


def test_apply_plus_and_minus1():
    """Check a simple expression."""
    parser = Parser(get_token("10-5+2"))
    ast = parser._expr()
    visitor = CalculationVisitor(global_scope={})

    assert visitor.visit(ast) == 7


def test_apply_plus_and_minus2():
    """Check a simple expression."""
    parser = Parser(get_token("10-2-5+2"))
    ast = parser._expr()
    visitor = CalculationVisitor(global_scope={})

    assert visitor.visit(ast) == 5


def test_apply_plus_and_multiply():
    """Check a simple expression."""
    parser = Parser(get_token("10+2*3"))
    ast = parser._expr()
    visitor = CalculationVisitor(global_scope={})

    assert visitor.visit(ast) == 16


def test_apply_minus_and_multiply():
    """Check a simple expression."""
    parser = Parser(get_token("10-2*3"))
    ast = parser._expr()
    visitor = CalculationVisitor(global_scope={})

    assert visitor.visit(ast) == 4


def test_apply_multiply():
    """Check a simple expression."""
    parser = Parser(get_token("10*2*3"))
    ast = parser._expr()
    visitor = CalculationVisitor(global_scope={})

    assert visitor.visit(ast) == 60


def test_plus_and_multiply2():
    """Check a simple expression."""
    parser = Parser(get_token("(10+2)*3"))
    ast = parser._expr()
    visitor = CalculationVisitor(global_scope={})

    assert visitor.visit(ast) == 36


def test_minus_and_multiply2():
    """Check a simple expression."""
    parser = Parser(get_token("(10-2)*3"))
    ast = parser._expr()
    visitor = CalculationVisitor(global_scope={})

    assert visitor.visit(ast) == 24


def test_plus_and_divide():
    """Check a simple expression."""
    parser = Parser(get_token("2+10/2"))
    ast = parser._expr()
    visitor = CalculationVisitor(global_scope={})

    assert visitor.visit(ast) == 7


def test_minus_and_divide():
    """Check a simple expression."""
    parser = Parser(get_token("2-10/2"))
    ast = parser._expr()
    visitor = CalculationVisitor(global_scope={})

    assert visitor.visit(ast) == -3


def test_minus_and_divide2():
    """Check a simple expression."""
    parser = Parser(get_token("(20-10)/2"))
    ast = parser._expr()
    visitor = CalculationVisitor(global_scope={})

    assert visitor.visit(ast) == 5


def test_plus_and_divide2():
    """Check a simple expression."""
    parser = Parser(get_token("(20+10)/2"))
    ast = parser._expr()
    visitor = CalculationVisitor(global_scope={})

    assert visitor.visit(ast) == 15


def test_unary():
    """Check a simple expression."""
    parser = Parser(get_token("-2"))
    ast = parser._expr()
    visitor = CalculationVisitor(global_scope={})

    assert visitor.visit(ast) == -2


def test_unary2():
    """Check a simple expression."""
    parser = Parser(get_token("+2"))
    ast = parser._expr()
    visitor = CalculationVisitor(global_scope={})

    assert visitor.visit(ast) == 2


def test_unary3():
    """Check a simple expression."""
    parser = Parser(get_token("--2"))
    ast = parser._expr()
    visitor = CalculationVisitor(global_scope={})

    assert visitor.visit(ast) == 2


def test_unary4():
    """Check a simple expression."""
    parser = Parser(get_token("-+2"))
    ast = parser._expr()
    visitor = CalculationVisitor(global_scope={})

    assert visitor.visit(ast) == -2


def test_unary5():
    """Check a simple expression."""
    parser = Parser(get_token("-(+2)"))
    ast = parser._expr()
    visitor = CalculationVisitor(global_scope={})

    assert visitor.visit(ast) == -2


def test_unary6():
    """Check a simple expression."""
    parser = Parser(get_token("-(-2)"))
    ast = parser._expr()
    visitor = CalculationVisitor(global_scope={})

    assert visitor.visit(ast) == 2


def test_plus_and_divide_and_unary():
    """Check a simple expression."""
    parser = Parser(get_token("(20+10)/(-2)"))
    ast = parser._expr()
    visitor = CalculationVisitor(global_scope={})

    assert visitor.visit(ast) == -15


def test_plus_and_divide_and_unary2():
    """Check a simple expression."""
    parser = Parser(get_token("(20+10)/(+2)"))
    ast = parser._expr()
    visitor = CalculationVisitor(global_scope={})

    assert visitor.visit(ast) == 15


def test_assign_operator():
    """Check a simple expression."""
    parser = Parser(get_token("a:=2"))
    ast = parser._assignment_statement()

    global_scope = {}
    visitor = CalculationVisitor(global_scope)
    visitor.visit(ast)

    assert global_scope["a"] == 2


def test_compound_operator1():
    """Check a simple expression."""
    parser = Parser(get_token("BEGIN a:=2 END"))
    ast = parser._compound_statement()

    global_scope = {}
    visitor = CalculationVisitor(global_scope)
    visitor.visit(ast)

    assert global_scope["a"] == 2


def test_compound_operator2():
    """Check a simple expression."""
    parser = Parser(get_token("BEGIN a:=2; b:=3; END"))
    ast = parser._compound_statement()

    global_scope = {}
    visitor = CalculationVisitor(global_scope)
    visitor.visit(ast)

    assert global_scope["a"] == 2
    assert global_scope["b"] == 3


def test_compound_operator3():
    """Check a simple expression."""
    parser = Parser(get_token("BEGIN a:=2; a:=3; END"))
    ast = parser._compound_statement()

    global_scope = {}
    visitor = CalculationVisitor(global_scope)
    visitor.visit(ast)

    assert global_scope["a"] == 3
    assert len(global_scope) == 1


def test_compound_operator4():
    """Check a simple expression."""
    parser = Parser(get_token("BEGIN a:=10+15*2; b:=10-100/2; END"))
    ast = parser._compound_statement()

    global_scope = {}
    visitor = CalculationVisitor(global_scope)
    visitor.visit(ast)

    assert global_scope["a"] == 40
    assert global_scope["b"] == -40


def test_compound_operator5():
    """Check a simple expression."""
    parser = Parser(get_token("BEGIN a:=10+15*2; b:=10-100/2; c:=10--2 END"))
    ast = parser._compound_statement()

    global_scope = {}
    visitor = CalculationVisitor(global_scope)
    visitor.visit(ast)

    assert global_scope["a"] == 40
    assert global_scope["b"] == -40
    assert global_scope["c"] == 12
