# Task 2: Functional Language Interpreter ⏳ IN PROGRESS

## Overview

An interpreter for a dynamically-typed functional programming language with lambda calculus features. The language supports functions as first-class values, structured data (records), and eager/lazy evaluation strategies.

## Assignment Requirements ✅ COMPLIANCE

**Implementation Constraints:**
- ✅ **Dynamically typed language**: Python implementation
- ✅ **Minimal subset**: Focus on core functional features
- ✅ **Simple syntax/semantics**: Avoid complex compiler technologies
- ✅ **Lambda calculus foundation**: Functions, application, variables
- ✅ **Structured data**: Records and lists

## Language Specification

### Core Language Elements

#### **1. Integers**
```
42
-17
0
```

#### **2. Functions (Lambda Abstractions)**
```
x.x                           # Identity function
x.mult x x                    # Square function  
x.y.add x y                   # Two-parameter function (curried)
```

#### **3. Function Application**
```
(x.mult x x) 2                # Apply square to 2 → 4
(x.y.add x y) 3 5             # Apply add to 3 and 5 → 8
```

#### **4. Variables and Naming**
```
x                             # Variable reference
plus                          # Built-in function reference
```

#### **5. Records (Structured Data)**

**Lazy Records `{...}`** - Evaluated on demand:
```
{d=x.mult x x, v=d 2}         # d not evaluated until accessed
```

**Eager Records `[...]`** - Evaluated immediately:
```
[d=x.mult x x, v=d 2]         # v becomes 4 immediately
```

**Record Application** - Creates environments:
```
[a=5, b=10] add a b           # Uses local bindings → 15
```

#### **6. Predefined Operations**
- `plus` - Addition
- `minus` - Subtraction  
- `mult` - Multiplication
- `div` - Division
- `cond` - Conditional (lazy evaluation of branches)

### Syntax Grammar (EBNF)

```ebnf
<expr> ::= <apply>
         | <name> '.' <expr>

<apply> ::= <basic>
          | <apply> <basic>

<basic> ::= <integer>
          | <name>
          | '(' <expr> ')'
          | '{' [<pairs>] '}'
          | '[' [<pairs>] ']'

<pairs> ::= <name> '=' <expr>
          | <pairs> ',' <name> '=' <expr>
```

## Example Programs

### **Basic Evaluation**
```python
# Simple values
42                            # → 42
x.x                          # → <function>

# Function application
(x.mult x x) 5               # → 25
(x.y.plus x y) 3 4           # → 7
```

### **Records and Environments**
```python
# Lazy record
{a=5, b=mult a 2}            # b not evaluated yet

# Eager record  
[a=5, b=mult a 2]            # b = 10 immediately

# Environment application
[x=10, y=20] plus x y        # → 30
```

### **Complex Example (Assignment)**
```python
{
  list=c.f.x.cond (c x)
    [val=x, nxt=list c f (f x)]
    [],
  reduce=f.x.l.cond l
    (f (reduce f x (l nxt)) (l val))
    x,
  range=a.b.list (x.minus b x) (x.plus 1 x) a,
  sum=l.reduce (x.y.plus x y) 0 l
}
sum (range 3 6)              # → 12 (sum of 3,4,5)
```

## Implementation Architecture

### **Core Components**

#### **1. Lexer (`lexer.py`)**
- Tokenize input into symbols, numbers, keywords
- Handle parentheses, braces, dots, commas
- Skip whitespace and comments

#### **2. Parser (`parser.py`)**  
- Recursive descent parser
- Build Abstract Syntax Tree (AST)
- Handle operator precedence and associativity

#### **3. AST Nodes (`ast_nodes.py`)**
```python
class ASTNode: pass
class Integer(ASTNode): value
class Variable(ASTNode): name
class Lambda(ASTNode): param, body
class Application(ASTNode): func, arg
class Record(ASTNode): bindings, eager
class RecordAccess(ASTNode): record, field
```

#### **4. Environment (`environment.py`)**
- Variable scoping and binding
- Record-based environments
- Built-in function definitions

#### **5. Evaluator (`evaluator.py`)**
- Recursive evaluation of AST
- Lazy vs eager evaluation strategies
- Function application and closure creation

#### **6. Built-ins (`builtins.py`)**
- Predefined functions: `plus`, `minus`, `mult`, `div`, `cond`
- Special conditional evaluation logic

### **Value Types**
```python
class Value: pass
class IntegerValue(Value): value
class FunctionValue(Value): param, body, env
class RecordValue(Value): bindings, eager
class BuiltinValue(Value): name, func
```

## Evaluation Strategy

### **Default: Eager Evaluation**
- Expressions evaluated immediately when encountered
- Function arguments evaluated before application
- Record values computed when record is created (for eager records)

### **Lazy Evaluation Cases**
1. **Lazy records `{...}`**: Bindings evaluated only when accessed
2. **Conditional branches**: `cond b t f` only evaluates relevant branch
3. **Function bodies**: Evaluated only when function is applied

### **Scoping Rules**
- **Lexical scoping** for function parameters
- **Dynamic environments** from record application
- **Built-ins** available in all scopes

## Testing Strategy

### **Unit Tests**
```python
# Basic evaluation
test_integer_literal()
test_variable_lookup()
test_function_definition()
test_function_application()

# Advanced features  
test_lazy_records()
test_eager_records()
test_conditional_evaluation()
test_currying()
```

### **Integration Tests**
```python
# Assignment examples
test_simple_arithmetic()
test_record_environments()
test_range_sum_example()
```

### **Error Handling Tests**
```python
test_undefined_variable()
test_type_errors()
test_syntax_errors()
```

## Usage

### **Run Interpreter**
```bash
# Interactive mode
python interpreter.py

# Execute file
python interpreter.py examples/factorial.func

# Run tests
python test_interpreter.py
```

### **Interactive Session**
```
Functional Language Interpreter v1.0
> (x.mult x x) 5
25
> [a=10, b=20] plus a b  
30
> cond 1 42 0
42
> quit
```

## File Structure
```
task2/
├── interpreter.py            # Main interpreter entry point
├── lexer.py                 # Tokenization
├── parser.py                # Parsing to AST
├── ast_nodes.py             # AST node definitions
├── evaluator.py             # Expression evaluation
├── environment.py           # Scoping and environments
├── builtins.py              # Built-in functions
├── values.py                # Value type definitions
├── test_interpreter.py      # Comprehensive test suite
├── examples/                # Example programs
│   ├── basic.func           # Simple examples
│   ├── factorial.func       # Factorial computation
│   ├── fibonacci.func       # Fibonacci sequence
│   └── assignment.func      # Range/sum from assignment
└── README.md               # This documentation
```

## Implementation Phases

### **Phase 1: Core Interpreter ⏳**
- [x] Project setup and structure
- [x] Lexer implementation
- [x] Basic parser (integers, variables)
- [x] Simple evaluator
- [x] Basic function definition/application

### **Phase 2: Advanced Features ⏳**
- [ ] Record support (lazy/eager)
- [ ] Built-in functions
- [ ] Conditional evaluation
- [ ] Environment management

### **Phase 3: Complete Language ⏳**
- [ ] Complex nested structures
- [ ] Assignment example working
- [ ] Comprehensive error handling
- [ ] Full test coverage

## Development Guidelines

### **Code Quality**
- **Clear, readable code** with comprehensive comments
- **Modular design** with separated concerns
- **Comprehensive testing** for all features
- **Error handling** with informative messages

### **Testing Requirements**
- **Unit tests** for each component
- **Integration tests** for complete programs
- **Assignment example** must work correctly
- **Edge cases** and error conditions covered

### **Documentation**
- **Inline code documentation**
- **Usage examples** for all features
- **Architecture explanation**
- **Testing instructions**

## Assignment Compliance

| Requirement | Status | Implementation |
|-------------|--------|----------------|
| Integers | ✅ | Integer literals and arithmetic |
| Structured data | ⏳ | Records with lazy/eager evaluation |
| Functions | ⏳ | Lambda abstractions with closures |
| Named entities | ⏳ | Variable binding and lookup |
| Predefined operations | ⏳ | Built-in arithmetic and conditionals |
| Dynamically typed | ✅ | Python implementation |
| Simple syntax | ✅ | Minimal grammar without complex tools |
| Assignment example | ⏳ | Range/sum program working |

## Success Criteria

**Minimum Viable Implementation:**
- ✅ Basic function definition and application
- ✅ Integer arithmetic with built-ins
- ✅ Simple record creation and access
- ✅ Variable scoping and environments
- ✅ Assignment example executes correctly

**Complete Implementation:**
- ✅ All language features working
- ✅ Lazy vs eager evaluation implemented
- ✅ Comprehensive test coverage
- ✅ Error handling and edge cases
- ✅ Clean, well-documented code

**🎯 Target: Functional interpreter demonstrating core concepts of functional programming while maintaining simplicity and clarity.**