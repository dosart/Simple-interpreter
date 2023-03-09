# -*- coding:utf-8 -*-

"""Parser's implementation."""

from interpreter.ast import (
    BinaryOperation,
    Num,
    CompoundOperator,
    AssiginOperator,
    Variable,
    EmptyOperator,
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
        node = self._program()
        if self.current_token.type != TokenType.eof:
            self._error()
        return node

    def _program(self):
        node = self._compound_statement()
        self._eat(TokenType.dot)
        return node

    def _compound_statement(self):
        self._eat(TokenType.begin)
        nodes = self._statement_list()
        self.eat(TokenType.end)
        root = CompoundOperator()

        for node in nodes:
            root.children.append(node)

    def _statement_list(self):
        node = self._statement()
        statements = [node]

        while self.current_token.type == TokenType.semi:
            self.eat(TokenType.semi)
            statements.append(self._statement())
        return statements

    def _statement(self):
        if self.current_token.type == TokenType.begin:
            node = self._compound_statement()
        elif self.current_token.type == TokenType.variable:
            node = self._assignment_statement()
        else:
            node = self._empty()
        return node

    def _assignment_statement(self):
        variable = self._variable()
        assignment_operator = self.current_token
        self.eat(TokenType.assigin)
        expression = self._expr()
        return AssiginOperator(variable, assignment_operator, expression)

    def _variable(self):
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
            factor : INTEGER | LPAREN expr RPAREN
        """
        token = self.current_token
        if token.type == TokenType.integer:
            self._eat(TokenType.integer)
            return Num(token)
        elif token.type == TokenType.lparen:
            self._eat(TokenType.lparen)
            node = self.expr()
            self._eat(TokenType.rparen)
            return node
        else:
            return self._variable()

    def _eat(self, token_type):
        """Compare the current token type with the passed token.

        Args:
            token_type: error message or correct value
        """
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
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
