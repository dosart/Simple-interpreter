# -*- coding:utf-8 -*-

"""Parser's implementation."""

from interpreter.ast import BinaryOperation, Num
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
        return self._expr()

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
