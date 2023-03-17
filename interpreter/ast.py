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

    def __str__(self):
        """Represent object as a string.

        Returns:
            str: Num as a string

        """
        return "Num({value})".format(value=self.value)

    def __repr__(self):
        """Represent object as a string.

        Returns:
            str: Num as a string

        """
        return str(self)


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

    def __str__(self):
        """Represent object as a string.

        Returns:
            str: BinaryOperation as a string

        """
        return "BinaryOperation({left_child} {operator} {right_child})".format(
            operator=self.op.value,
            left_child=self.left,
            right_child=self.right,
        )

    def __repr__(self):
        """Represent object as a string.

        Returns:
            str: BinaryOperation as a string

        """
        return str(self)


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

    def __str__(self):
        """Represent object as a string.

        Returns:
            str: UnaryOperation as a string

        """
        return "UnaryOperation({operator} {expression})".format(
            operator=self.op.value,
            expression=self.expr,
        )

    def __repr__(self):
        """Represent object as a string.

        Returns:
            str: UnaryOperation as a string

        """
        return str(self)


class CompoundOperator(AST):
    """Represents a 'BEGIN ... END' block."""

    def __init__(self):
        """Construct a new iterator."""
        self._statement_list = []

    def set_compound_statement(self, compound_statement):
        """Add statement in list.

        Args:
            compound_statement: list of operators(node that implements the operator ast)

        """
        for statement in compound_statement:
            self._statement_list.append(statement)

    def add_statement(self, statement):
        """Add statement in list.

        Args:
            statement: any node that implements the operator ast

        """
        self._statement_list.append(statement)

    @property
    def compound_statement(self):
        """Return list of statement.

        Returns:
            list: list of statement

        """
        return self._statement_list

    def __str__(self):
        """Represent object as a string.

        Returns:
            str: CompoundOperator as a string

        """
        return "CompoundOperator(BEGIN {statement_list} END)".format(
            statement_list=" ".join(
                str(statement) for statement in self._statement_list
            ),
        )

    def __repr__(self):
        """Represent object as a string.

        Returns:
            str: CompoundOperator as a string

        """
        return str(self)


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

    def __str__(self):
        """Represent object as a string.

        Returns:
            str: AssignOperator as a string

        """
        return "AssignOperator({variable} {operator} {expression})".format(
            variable=self.variable,
            operator=self.op.value,
            expression=self.expr,
        )

    def __repr__(self):
        """Represent object as a string.

        Returns:
            str: AssignOperator as a string

        """
        return str(self)


class Variable(AST):
    """Implementation of variable."""

    def __init__(self, token):
        """Construct a new variable.

        Args:
            token: variable token(type is TokenType.variable)
        """
        self.token = token
        self.value = token.value

    def __str__(self):
        """Represent object as a string.

        Returns:
            str: Variable as a string

        """
        return "Variable({variable})".format(variable=self.value)

    def __repr__(self):
        """Represent object as a string.

        Returns:
            str: Variable as a string

        """
        return str(self)


class EmptyOperator:
    """Implementation of the AST base class."""

    pass
