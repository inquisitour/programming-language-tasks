from lexer import Lexer, Token
from ast_nodes import Integer, Variable, Lambda, Application

class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = lexer.get_next_token()
        self.peek_token = lexer.get_next_token()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.peek_token
            self.peek_token = self.lexer.get_next_token()
        else:
            raise SyntaxError(f'Expected {token_type}, got {self.current_token.type}')

    def parse_expr(self):
        # Lambda abstraction: name '.' expr
        if self.current_token.type == Token.NAME and self.peek_token.type == Token.DOT:
            param = self.current_token.value
            self.eat(Token.NAME)
            self.eat(Token.DOT)
            body = self.parse_expr()
            return Lambda(param, body)
        return self.parse_apply()

    def parse_apply(self):
        node = self.parse_basic()
        # Left-associative application
        while self.current_token.type in (Token.INTEGER, Token.NAME, Token.LPAREN):
            right = self.parse_basic()
            node = Application(node, right)
        return node

    def parse_basic(self):
        token = self.current_token
        if token.type == Token.INTEGER:
            self.eat(Token.INTEGER)
            return Integer(token.value)
        if token.type == Token.NAME:
            self.eat(Token.NAME)
            return Variable(token.value)
        if token.type == Token.LPAREN:
            self.eat(Token.LPAREN)
            node = self.parse_expr()
            self.eat(Token.RPAREN)
            return node
        raise SyntaxError(f'Unexpected token: {token}')
