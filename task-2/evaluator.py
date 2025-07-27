from ast_nodes import Integer, Variable, Lambda, Application
from environment import Environment
from values import IntegerValue, FunctionValue

class Evaluator:
    def __init__(self):
        self.global_env = Environment()

    def eval(self, node, env=None):
        if env is None:
            env = self.global_env
        if isinstance(node, Integer):
            return IntegerValue(node.value)
        if isinstance(node, Variable):
            return env.lookup(node.name)
        if isinstance(node, Lambda):
            return FunctionValue(node.param, node.body, env)
        if isinstance(node, Application):
            func_val = self.eval(node.func, env)
            arg_val = self.eval(node.arg, env)
            if not isinstance(func_val, FunctionValue):
                raise TypeError('Attempt to call a non-function')
            new_env = func_val.env.extend(func_val.param, arg_val)
            return self.eval(func_val.body, new_env)
        raise TypeError(f'Unknown AST node: {type(node)}')
