# Programming Languages Course (LVA 185.208)

This repository contains implementations for three programming language assignments from TU Wien.

## Overview

**Task 1**: Stack-based Calculator with Post-fix Notation  
**Task 2**: Functional Language Interpreter  
**Task 3**: Syntax-aware Editor for Task 2 Language  

## Task 1: Programmable Calculator

### Description
A post-fix notation calculator using stack-based evaluation with programmable capabilities.

### Features
- Post-fix expression evaluation (`5.1 12.3 +` → `17.4`)
- Stack-based architecture with operation modes
- 52 registers (A-Z, a-z) for storing values/programs
- String execution with `@` and `\` operators
- Interactive REPL with startup program

### Key Operations
- **Arithmetic**: `+`, `-`, `*`, `/`, `%`
- **Comparison**: `=`, `<`, `>`
- **Logic**: `&`, `|`
- **Stack**: `!` (copy), `$` (delete), `#` (size)
- **I/O**: `'` (input), `"` (output)
- **Execution**: `@` (immediate), `\` (deferred)

### Usage
```
python calculator.py
```

## Task 2: Functional Language Interpreter

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

### Usage
```
python interpreter.py [file.func]
```

## Task 3: Syntax-aware Editor

### Description
Smart editor for the functional language with syntax highlighting and error detection.

### Features
- Syntax error highlighting (unbalanced braces)
- Name occurrence highlighting
- Matching brace highlighting
- Optional program execution

### Implementation
- Language: Haskell (GHC)
- Terminal-based interface
- Real-time syntax analysis

### Usage
```
ghc editor.hs -o editor
./editor [filename]
```

## File Structure
```
├── task1/
│   ├── calculator.py
│   ├── tests/
│   └── README.md
├── task2/
│   ├── interpreter.py
│   ├── examples/
│   └── README.md
├── task3/
│   ├── editor.hs
│   ├── src/
│   └── README.md
└── README.md
```

## Testing

Each task includes comprehensive tests demonstrating the required functionality:

- **Task 1**: Interactive calculator with string analysis program
- **Task 2**: Functional programs including recursion and data structures  
- **Task 3**: Editor testing with syntax highlighting examples

## Requirements

- **Task 1 & 2**: Python 3.7+
- **Task 3**: GHC 8.6+ (Haskell)

## Assignment Specifications

Full specifications available in the `docs/` directory containing the original PDF requirements.
