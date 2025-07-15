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
- **Stack**: `!` (copy), `# Programming Languages Course (LVA 185.208)

This repository contains implementations for three programming language assignments from TU Wien.

## Overview

**Task 1**: Stack-based Calculator with Post-fix Notation  
**Task 2**: Functional Language Interpreter  
**Task 3**: Syntax-aware Editor for Task 2 Language  

 (delete), `#` (size)
- **I/O**: `'` (input), `"` (output)
- **Execution**: `@` (immediate), `\` (deferred)

### Quick Test
```bash
cd task1/
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
📝 String operations: ✅ Working  
🗂️ All 52 registers: ✅ Present
🚀 Startup program: ✅ Verified
```

## Task 2: Functional Language Interpreter ⏳ PENDING

**📖 [Task 2 Documentation](task2/README.md)** *(Will be created)*

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
- 🔄 **In Progress**: Starting implementation
- 📋 **Language**: Python (dynamically typed as required)
- 🎯 **Target**: Lambda calculus with records and eager evaluation

## Task 3: Syntax-aware Editor ⏳ PENDING

**📖 [Task 3 Documentation](task3/README.md)** *(Will be created)*

### Description
Smart editor for the functional language with syntax highlighting and error detection.

### Features
- Syntax error highlighting (unbalanced braces)
- Name occurrence highlighting
- Matching brace highlighting
- Optional program execution

### Implementation Status
- ⏸️ **Waiting**: Depends on Task 2 completion
- 📋 **Language**: Haskell (GHC)
- 🎯 **Target**: Terminal-based functional editor

## File Structure
```
├── task1/ ✅ COMPLETE
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
├── task2/ ⏳ IN PROGRESS
│   ├── interpreter.py            # Will be implemented
│   ├── examples/                 # Example programs
│   └── README.md                 # 📖 Task 2 documentation (TBD)
├── task3/ ⏳ PENDING
│   ├── editor.hs                 # Will be implemented
│   ├── src/                      # Haskell modules
│   └── README.md                 # 📖 Task 3 documentation (TBD)
└── README.md                     # 📖 This overview document
```

## Quick Navigation

- **📖 [Task 1: Post-fix Calculator](task1/README.md)** - Complete implementation with full testing
- **📖 [Task 2: Functional Interpreter](task2/README.md)** - *(To be created)*
- **📖 [Task 3: Syntax Editor](task3/README.md)** - *(To be created)*

## Testing

### Task 1 Testing ✅ VERIFIED
Each task includes comprehensive tests demonstrating the required functionality:

**Quick Verification:**
```bash
cd task1/
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

### Task 2 & 3 Testing
- 🔄 **In Progress**: Test suites will be developed alongside implementation

## Requirements

- **Task 1**: Python 3.7+ ✅ VERIFIED
- **Task 2**: Python 3.7+ (dynamically typed as specified)
- **Task 3**: GHC 8.6+ (Haskell)

## Current Status

| Task | Status | Completion | Tests |
|------|--------|------------|-------|
| Task 1: Calculator | ✅ COMPLETE | 100% | 8/8 examples passing |
| Task 2: Interpreter | ⏳ STARTING | 0% | - |
| Task 3: Editor | ⏳ PENDING | 0% | - |

## Assignment Specifications

Full specifications available in the `docs/` directory containing the original PDF requirements.

**Task 1 Achievement**: 🎯 **ALL ASSIGNMENT REQUIREMENTS SATISFIED**
- Post-fix notation working perfectly
- Stack evaluation exactly as specified  
- String execution with calculator language programs
- 52 registers with startup and analysis programs
- Complete test coverage with multiple verification methods
