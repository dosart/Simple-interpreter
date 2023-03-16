# -*- coding:utf-8 -*-

"""Abstract Syntax Tree's implementation."""


class AST(object):
    """Implementation of the AST base class."""

    pass


class Num(AST):
    """Implementation of the Int class."""

    def __init__(self, token):
        """Construct a new int object.

        Args:
            token: integer token
        """
        self.token = token
        self.value = token.value

    def __repr__(self):
        """Represent object as a string.

        Returns:
            str: represent object as a string

        """
        return "Num({value})".format(value=self.value)


class BinaryOperation(AST):
    """Implementation of the binary operator."""

    def __init__(self, left, op, right):
        """Construct a new binary operator.

        Args:
            left: integer token
            op: operator token
            right: integer token
        """
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        """Represent object as a string.

        Returns:
            str: represent object as a string

        """
        return "BinaryOperation({operator}, {left_child}, {right_child})".format(
            operator=self.op,
            left_child=self.left,
            right_child=self.right,
        )


class UnaryOperation(AST):
    """Implementation of the unary operator."""

    def __init__(self, op, expr):
        """Construct a new unary operator.

        Args:
            op: operator token
            expr: expression to evaluate
        """
        self.op = op
        self.expr = expr

    def __repr__(self):
        """Represent object as a string.

        Returns:
            str: represent object as a string

        """
        return "UnaryOperation({operator}, {expression})".format(
            operator=self.op,
            expression=self.right,
        )


class CompoundOperator(AST):
    """Represents a 'BEGIN ... END' block"""

    def __init__(self):
        self._statement_list = []

    def set_compound_statement(self, compound_statement):
        for statement in compound_statement:
            self._statement_list.append(statement)

    @property
    def compound_statement(self):
        return self._statement_list


class AssignOperator(AST):
    """Implementation of assign operator."""

    def __init__(self, variable, op, expr):
        """Construct a new assign operator.

        Args:
            variable (Variable): variable node
            op: operator token
            expr: expression to evaluate (BinaryOperation or UnaryOperation or Num)
        """
        self.variable = variable
        self.op = op
        self.expr = expr

    def __repr__(self):
        """Represent object as a string.

        Returns:
            str: represent object as a string

        """
        return "AssignOperator({variable}, {operator},  {expression})".format(
            variable=self.variable,
            operator=self.op,
            right_child=self.expr,
        )


class Variable(AST):
    """Implementation of variable."""

    def __init__(self, token):
        """Construct a new variable.

        Args:
            token: variable token(type is TokenType.variable)
        """
        self.token = token
        self.value = token.value


class EmptyOperator:
    """Implementation of the AST base class."""

    pass
