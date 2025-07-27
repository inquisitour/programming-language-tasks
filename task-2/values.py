class Value:
    pass

class IntegerValue(Value):
    def __init__(self, value):
        self.value = value

class FunctionValue(Value):
    def __init__(self, param, body, env):
        self.param = param
        self.body = body
        self.env = env
