class Token:
    INTEGER = 'INTEGER'
    NAME = 'NAME'
    DOT = 'DOT'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    EOF = 'EOF'

    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {self.value})'

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = text[self.pos] if text else None

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def name(self):
        result = ''
        while self.current_char is not None and self.current_char.isalpha():
            result += self.current_char
            self.advance()
        return result

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(Token.INTEGER, self.integer())

            if self.current_char.isalpha():
                return Token(Token.NAME, self.name())

            if self.current_char == '.':
                self.advance()
                return Token(Token.DOT, '.')
            if self.current_char == '(':
                self.advance()
                return Token(Token.LPAREN, '(')
            if self.current_char == ')':
                self.advance()
                return Token(Token.RPAREN, ')')

            raise SyntaxError(f'Unknown character: {self.current_char}')

        return Token(Token.EOF, None)