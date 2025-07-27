class ASTNode:
    pass

class Integer(ASTNode):
    def __init__(self, value):
        self.value = value

class Variable(ASTNode):
    def __init__(self, name):
        self.name = name

class Lambda(ASTNode):
    def __init__(self, param, body):
        self.param = param
        self.body = body

class Application(ASTNode):
    def __init__(self, func, arg):
        self.func = func
        self.arg = arg