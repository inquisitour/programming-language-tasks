class Environment:
    def __init__(self, parent=None):
        self.bindings = {}
        self.parent = parent

    def lookup(self, name):
        if name in self.bindings:
            return self.bindings[name]
        if self.parent:
            return self.parent.lookup(name)
        raise NameError(f'Unbound variable: {name}')

    def extend(self, name, value):
        new_env = Environment(parent=self)
        new_env.bindings[name] = value
        return new_env
