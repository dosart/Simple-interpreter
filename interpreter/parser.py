# -*- coding:utf-8 -*-

"""Parser's implementation."""

from interpreter.ast import (
    AssiginOperator,
    BinaryOperation,
    CompoundOperator,
    EmptyOperator,
    Num,
    UnaryOperation,
    Variable,
)
from interpreter.token import TokenType


class Parser(object):
    """The Parser class is used to build an abstract syntax tree from stream token.

    Attributes:
        lexer: return a token from a stream
        current_token: pointer to the currently processed token

    Methods:
        parse(): return ATS from stream token

    """

    def __init__(self, lexer):
        """Construct a new parser.

        Args:
            lexer: it can return a token from a stream
        """
        self.lexer = lexer
        self.current_token = next(lexer)

    def parse(self):
        """Return AST from stream token.

        Returns:
            tree: abstract syntax tree of expression
        """
        ast = self._program()
        if self.current_token.type != TokenType.eof:
            self._error()
        return ast

    def _program(self):
        """Return the result of a nonterminal term.

        Returns:
            program : compound statement DOT
        """
        ast = self._compound_statement()
        self._eat(TokenType.dot)
        return ast

    def _compound_statement(self):
        """Return the result of a nonterminal term.

        Returns:
            compound statement : BEGIN statement list END
        """
        self._eat(TokenType.begin)

        root = CompoundOperator()
        root.set_compound_statement(self._statement_list())

        self._eat(TokenType.end)
        return root

    def _statement_list(self):
        """Return the result of a nonterminal term.

        Returns:
            statement list : statement |
                             statement SEMI statement list
        """
        statements = [self._statement()]

        while self.current_token.type == TokenType.semi:
            self._eat(TokenType.semi)
            statements.append(self._statement())
        return statements

    def _statement(self):
        """Return the result of a nonterminal term.

        Returns:
            statement : compound_statement   |
                        assignment_statement |
                        empty
        """
        if self.current_token.type == TokenType.begin:
            return self._compound_statement()
        elif self.current_token.type == TokenType.variable:
            return self._assignment_statement()
        return self._empty()

    def _assignment_statement(self):
        """Return the result of a nonterminal term.

        Returns:
            assignment_statement : variable := expr
        """
        variable = self._variable()
        assignment_operator = self.current_token
        self._eat(TokenType.assigin)
        expression = self._expr()
        return AssiginOperator(variable, assignment_operator, expression)

    def _variable(self):
        """Return the result of a nonterminal term.

        Returns:
            variable : ^[a-zA-Z]+$
        """
        node = Variable(self.current_token)
        self._eat(TokenType.variable)
        return node

    def _empty(self):
        return EmptyOperator()

    def _expr(self):
        """Return the result of a nonterminal term.

        Returns:
            expr   : term ((PLUS | MINUS) term)*
            term   : factor ((MUL | DIV) factor)*
            factor : INTEGER | LPAREN expr RPAREN
        """
        node = self._term()

        while self.current_token.type in {TokenType.plus, TokenType.minus}:
            token = self.current_token
            if token.type == TokenType.plus:
                self._eat(TokenType.plus)
            elif token.type == TokenType.minus:
                self._eat(TokenType.minus)

            node = BinaryOperation(left=node, op=token, right=self._term())

        return node

    def _term(self):
        """Return the result of a nonterminal term.

        Returns:
            term : factor ((MUL | DIV) factor)*
        """
        node = self._factor()
        while self.current_token.type in {TokenType.multiply, TokenType.divide}:
            token = self.current_token
            if token.type == TokenType.multiply:
                self._eat(TokenType.multiply)
            elif token.type == TokenType.divide:
                self._eat(TokenType.divide)

            node = BinaryOperation(left=node, op=token, right=self._factor())

        return node

    def _factor(self):
        """Return the result of a nonterminal factor.

        Returns:
            factor : plus  factor |
                     minus factor |
                     integer      |
                     lparen expr rparen |
                     variable
        """
        token = self.current_token
        if token.type == TokenType.plus:
            self._eat(TokenType.plus)
            return UnaryOperation(token, self._factor())
        elif token.type == TokenType.minus:
            self._eat(TokenType.minus)
            return UnaryOperation(token, self._factor())
        elif token.type == TokenType.integer:
            self._eat(TokenType.integer)
            return Num(token)
        elif token.type == TokenType.lparen:
            self._eat(TokenType.lparen)
            node = self._expr()
            self._eat(TokenType.rparen)
            return node
        return self._variable()

    def _eat(self, token_type):
        """Compare the current token type with the passed token.

        Args:
            token_type: error message or correct value
        """
        if self.current_token.type == token_type:
            self.current_token = next(self.lexer)
        else:
            self._error()

    def _error(self):
        """Raise exception.

        Raises:
            InvalidSyntaxError: raise exception
        """
        raise InvalidSyntaxError("Invalid syntax")


class InvalidSyntaxError(Exception):
    """Simple exception."""

    pass
