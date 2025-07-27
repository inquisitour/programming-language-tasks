from lexer import Lexer
from parser import Parser
from evaluator import Evaluator

class Interpreter:
    def __init__(self):
        self.evaluator = Evaluator()

    def eval_text(self, text: str):
        lexer = Lexer(text)
        parser = Parser(lexer)
        ast = parser.parse_expr()
        return self.evaluator.eval(ast)

if __name__ == '__main__':
    import sys
    text = sys.stdin.read().strip()
    result = Interpreter().eval_text(text)
    if hasattr(result, 'value'):
        print(result.value)
    else:
        print(result)