from ast_nodes import Integer, Variable, Lambda, Application, Record, Cond, Access
from environment import Environment
from values import IntegerValue, FunctionValue, BuiltinValue, RecordValue, Thunk
import builtins_lang as bl

class Evaluator:
    def __init__(self):
        self.global_env = Environment()
        for n, v in bl.get_builtins().items():
            self.global_env.bindings[n] = v

    def eval(self, node, env=None):
        if env is None:
            env = self.global_env

        # Integer literal
        if isinstance(node, Integer):
            return IntegerValue(node.value)

        # Variable lookup (force thunks)
        if isinstance(node, Variable):
            val = env.lookup(node.name)
            return val.force() if hasattr(val, 'force') else val

        # Lambda abstraction
        if isinstance(node, Lambda):
            return FunctionValue(node.param, node.body, env)

        # Conditional (lazy branches)
        if isinstance(node, Cond):
            cond_val = self.eval(node.cond, env)
            is_true = not (isinstance(cond_val, IntegerValue) and cond_val.value == 0)
            chosen = node.then if is_true else node.else_
            return self.eval(chosen, env)

        # Record literal
        if isinstance(node, Record):
            # Eager: left-to-right
            if node.eager:
                record_env = env
                vals = {}
                for name, expr in node.bindings:
                    val = self.eval(expr, record_env)
                    vals[name] = val
                    record_env = record_env.extend(name, val)
                return RecordValue(env, vals, {}, True)
            # Lazy: store exprs
            exprs = {name: expr for name, expr in node.bindings}
            return RecordValue(env, {}, exprs, False)

        # Field access
        if isinstance(node, Access):
            rv = self.eval(node.record, env)
            if not isinstance(rv, RecordValue):
                raise TypeError('Not a record')
            if rv.eager:
                return rv.vals[node.field]
            # lazy
            thunk = Thunk(rv.exprs[node.field], rv.env, self)
            val = thunk.force()
            rv.vals[node.field] = val
            return val

        # Function/Builtin/Record application
        if isinstance(node, Application):
            func_val = self.eval(node.func, env)
            # Built-in (curried)
            if isinstance(func_val, BuiltinValue):
                arg_val = self.eval(node.arg, env)
                if not isinstance(arg_val, IntegerValue):
                    raise TypeError('Built-in functions require integer args')
                args = func_val.args + [arg_val.value]
                if len(args) < func_val.arity:
                    return BuiltinValue(func_val.name, func_val.func, func_val.arity, args)
                return IntegerValue(func_val.func(*args))

            # Record application
            if isinstance(func_val, RecordValue):
                new_env = Environment(parent=func_val.env)
                if func_val.eager:
                    new_env.bindings.update(func_val.vals)
                else:
                    for name, expr in func_val.exprs.items():
                        new_env.bindings[name] = Thunk(expr, new_env, self)
                return self.eval(node.arg, new_env)

            # User-defined function
            if isinstance(func_val, FunctionValue):
                arg_val = self.eval(node.arg, env)
                new_env = func_val.env.extend(func_val.param, arg_val)
                return self.eval(func_val.body, new_env)

            raise TypeError('Cannot apply non-function')

        raise TypeError(f'Unknown node: {type(node)}')
