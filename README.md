# Programming Languages Course (LVA 185.208)

This repository contains implementations for three programming language assignments from TU Wien.

## Overview

**Task 1**: Stack-based Calculator with Post-fix Notation  
**Task 2**: Functional Language Interpreter  
**Task 3**: Syntax-aware Editor for Task 2 Language  

## Task 1: Programmable Calculator ✅ COMPLETED

**📖 [View Task 1 Documentation](task-1/README.md)**

### Description
A post-fix notation calculator using stack-based evaluation with programmable capabilities.

### Status: 🎯 ALL TESTS PASSING
- **Assignment Compliance**: 8/8 examples passing
- **Implementation**: 100% complete with all required features
- **Testing**: Comprehensive test suite with multiple verification methods

### Features
- Post-fix expression evaluation (`5.1 12.3 +` → `17.4`)
- Stack-based architecture with operation modes
- 52 registers (A-Z, a-z) for storing values/programs
- String execution with `@` and `\` operators
- Interactive REPL with startup program
- Complete string analysis program for word processing

### Key Operations
- **Arithmetic**: `+`, `-`, `*`, `/`, `%`
- **Comparison**: `=`, `<`, `>`
- **Logic**: `&`, `|`, `_` (null check), `~` (negate)
- **Stack**: `!` (copy), `$` (delete), `#` (size)
- **I/O**: `'` (input), `"` (output)
- **Execution**: `@` (immediate), `\` (deferred)

### Quick Test
```bash
cd task-1/
.\run_tests.bat                    # Windows all-in-one
python calculator.py -test         # Quick verification  
python calculator.py -i            # Interactive mode
```

### Verification Results
```
📊 Assignment Examples: 8/8 passed
🧮 All operators: ✅ Working
📝 String operations: ✅ Working  
🗂️ All 52 registers: ✅ Present
🚀 Startup program: ✅ Verified
```

## Task 2: Functional Language Interpreter ⏳ PENDING

**📖 [Task 2 Documentation](task-2/README.md)**

### Description
Interpreter for a dynamically-typed functional language with lambda calculus features.

### Language Features
- **Functions**: `x.mult x x` (lambda abstractions)
- **Application**: `(x.mult x x) 2` → `4`
- **Records**: 
  - Lazy: `{name=value, ...}`
  - Eager: `[name=value, ...]`
- **Predefined**: `plus`, `minus`, `mult`, `div`, `cond`

### Example Program
```
{
  range=a.b.list (x.minus b x) (x.plus 1 x) a,
  sum=l.reduce (x.y.plus x y) 0 l
}
sum (range 3 6)
```

### Implementation Status
- ✅ **Complete**: All features implemented and tested
- 📋 **Language**: Python (dynamically typed as required)
- 🎯 **Result**: Professional-grade functional interpreter with advanced features

## Task 3: Syntax-aware Editor ⏳ PENDING

**📖 [Task 3 Documentation](task-3/README.md)** *(Will be created)*

### Description
Smart editor for the functional language with syntax highlighting and error detection.

### Features
- Syntax error highlighting (unbalanced braces)
- Name occurrence highlighting
- Matching brace highlighting
- Optional program execution

### Implementation Status
- ⏸️ **Waiting**: Will soon start
- 📋 **Language**: Haskell (GHC)
- 🎯 **Target**: Terminal-based functional editor

## File Structure
```
├── task-1/ ✅ COMPLETE
│   ├── calculator.py              # Main implementation
│   ├── comprehensive_test.py      # Full compliance test
│   ├── simple_test.py            # Quick verification
│   ├── run_tests.bat             # Windows test runner
│   ├── tests/                    # Test suite
│   │   ├── test_calculator.py    # Unit tests
│   │   └── run_tests.py         # Test runner
│   ├── examples/                 # Examples and demos
│   │   └── string_analysis.py   # String analysis demo
│   └── README.md                 # 📖 Task 1 detailed documentation
├── task-2/ ✅ COMPLETE
│   ├── main.py                   # Main entry point with interactive mode
│   ├── interpreter.py            # Core interpreter interface
│   ├── lexer.py                 # Complete tokenization
│   ├── parser.py                # Recursive descent parser
│   ├── ast_nodes.py             # AST node definitions
│   ├── evaluator.py             # Advanced evaluation engine
│   ├── environment.py           # Scoping and environments
│   ├── builtins_lang.py         # Built-in functions
│   ├── values.py                # Value types + lazy evaluation
│   ├── test_comprehensive.py    # Full test suite (13/13 passing)
│   ├── examples/                # Working example programs
│   │   ├── basic.func           # Simple examples → 7
│   │   ├── square.func          # Lambda functions → 25
│   │   ├── currying.func        # Multi-parameter → 30
│   │   ├── records.func         # Record environments → 15
│   │   └── [3 more examples]    # All working perfectly
│   └── README.md                # 📖 Task 2 detailed documentation
├── task-3/ ⏳ PENDING
│   ├── editor.hs                 # Will be implemented
│   ├── src/                      # Haskell modules
│   └── README.md                 # 📖 Task 3 documentation (TBD)
└── README.md                     # 📖 This overview document
```

## Quick Navigation

- **📖 [Task 1: Post-fix Calculator](task-1/README.md)** - Complete implementation with full testing
- **📖 [Task 2: Functional Interpreter](task-2/README.md)** - Complete implementation with full testing
- **📖 [Task 3: Syntax Editor](task-3/README.md)** - *(To be created)*

## Testing

### Task 1 Testing ✅ VERIFIED
Each task includes comprehensive tests demonstrating the required functionality:

**Quick Verification:**
```bash
cd task-1/
.\run_tests.bat                    # Windows all-in-one test runner
python calculator.py -test         # Built-in quick tests
python simple_test.py              # Simple verification suite
```

**Comprehensive Testing:**
```bash
python comprehensive_test.py       # Full assignment compliance
python calculator.py -demo         # Feature demonstrations
python calculator.py -i            # Interactive testing
```

**Results Summary:**
- ✅ **Assignment Examples: 8/8 passing**
- ✅ **All operators verified**
- ✅ **String operations working**
- ✅ **Stack manipulation tested**
- ✅ **Register system verified**
- ✅ **Error handling confirmed**

### Task 2 Testing ✅ VERIFIED
Task 2 includes comprehensive tests demonstrating all functional programming features:

**Quick Verification:**
```bash
cd task-2/
python main.py                      # Interactive REPL
python test_comprehensive.py        # Full test suite
python main.py -demo                # Built-in demonstrations
```

**File Execution:**
```bash
python main.py examples/basic.func      # → 7
python main.py examples/square.func     # → 25
python main.py examples/currying.func   # → 30
python main.py examples/records.func    # → 15
```

**Results Summary:**
- ✅ **Assignment Tests: 13/13 passing**
- ✅ **All language elements verified**
- ✅ **Lazy/eager evaluation working**
- ✅ **Record environments tested**
- ✅ **Higher-order functions confirmed**
- ✅ **All example files working**

### Task 3 Testing
- 🔄 **Pending**: Test suite will be developed during implementation

## Requirements

- **Task 1**: Python 3.7+ ✅ VERIFIED
- **Task 2**: Python 3.7+ (dynamically typed as specified)
- **Task 3**: GHC 8.6+ (Haskell)

## Current Status

| Task | Status | Completion | Tests |
|------|--------|------------|-------|
| Task 1: Calculator | ✅ COMPLETE | 100% | 8/8 examples passing |
| Task 2: Interpreter | ✅ COMPLETE | 100% | 13/13 tests passing |
| Task 3: Editor | ⏳ PENDING | 0% | - |