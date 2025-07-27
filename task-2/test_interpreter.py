import unittest
from interpreter import Interpreter
from values import IntegerValue

class TestInterpreter(unittest.TestCase):
    def setUp(self):
        self.interpreter = Interpreter()

    def eval(self, text):
        result = self.interpreter.eval_text(text)
        if isinstance(result, IntegerValue):
            return result.value
        return result

    def test_integer(self):
        self.assertEqual(self.eval("42"), 42)

    def test_identity(self):
        self.assertEqual(self.eval("(x.x) 5"), 5)

    def test_const(self):
        self.assertEqual(self.eval("(x.(y.x)) 1 2"), 1)

    def test_unbound(self):
        with self.assertRaises(NameError):
            self.eval("x")

if __name__ == '__main__':
    unittest.main()