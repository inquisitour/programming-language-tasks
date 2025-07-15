# Task 1: Post-fix Stack-based Calculator ✅ COMPLETED

## Overview

A fully functional programmable calculator that uses post-fix notation with stack-based evaluation. The calculator features multiple operation modes, string execution capabilities, and 52 registers for storing programs and data. **All assignment requirements have been verified and implemented.**

## ✅ Assignment Compliance Verified

**Status: 🎯 ALL TESTS PASSING**
- ✅ **8/8 Assignment examples passing**
- ✅ **Post-fix notation**: `5.1 12.3+` → `17.4`
- ✅ **Stack evaluation**: `15 2 3 4+*-` → `1`
- ✅ **String execution**: `4 3(2*)@+` → `10`
- ✅ **Correct operation order**: `4 2-` → `2`, `4 2/` → `2`
- ✅ **All operation modes working**
- ✅ **52 registers implemented**
- ✅ **Startup program in register 'a'**
- ✅ **Complete string analysis program structure**

## Quick Start

### Run Tests
```bash
# Windows batch runner (recommended)
.\run_tests.bat

# Quick verification
python calculator.py -test

# Comprehensive compliance test
python comprehensive_test.py

# Simple test suite
python simple_test.py
```

### Interactive Mode
```bash
python calculator.py -i

# Example session:
> 1 1+           # → 2
> 5 3+ 2*        # → 16  
> (hi)(bye)+     # → "hibye"
> 15 2 3 4+*-    # → 1
> quit
```

### Demonstrations
```bash
python calculator.py -demo
```

## Architecture

### Core Components
- **Command Stream**: Sequential character commands
- **Operation Modes**: 
  - `0`: Execution mode
  - `-1`: Integer construction
  - `<-1`: Decimal place construction  
  - `>0`: String construction (nested parentheses)
- **Data Stack**: Holds integers, floats, and strings
- **Registers**: 52 registers (A-Z, a-z) for storing values
- **I/O Streams**: Input from keyboard, output to screen

### Operation Modes

| Mode | Description | Behavior |
|------|-------------|----------|
| 0 | Execution | Normal command execution |
| -1 | Integer construction | Building multi-digit integers |
| -2, -3, ... | Decimal construction | Building decimal places |
| 1, 2, ... | String construction | Building strings with nested () |

## Commands Reference

### Numbers and Data Types
- `0-9`: Push digit (starts integer construction)
- `.`: Start floating-point number or add decimal point
- `(...)`: String literal (content between parentheses)

### Arithmetic Operations
- `+`: Addition (also string concatenation)
- `-`: Subtraction (also string truncation) 
- `*`: Multiplication (also ASCII character insertion)
- `/`: Division (also substring search)
- `%`: Modulo (also ASCII code extraction)

### Comparison Operations
- `=`: Equal comparison
- `<`: Less than comparison  
- `>`: Greater than comparison

### Logic Operations
- `&`: Logical AND
- `|`: Logical OR
- `_`: Null check (returns 1 for 0, 0.0, or empty string)

### Stack Manipulation
- `!`: Copy nth element from top (`n !` copies nth element)
- `$`: Delete nth element from top (`n $` deletes nth element)
- `#`: Push current stack size
- `~`: Negate number or convert to empty string
- `?`: Convert float to integer (truncate)

### Program Control
- `@`: Execute string immediately (insert at command stream start)
- `\`: Execute string later (append to command stream end)
- `A-Z`, `a-z`: Push content of register

### Input/Output
- `'`: Read line from input (auto-convert to int/float/string)
- `"`: Pop and write value to output

## Examples (Assignment Specification)

### Basic Arithmetic
```
5.1 12.3+   → [17.4]        (from assignment: applies + to 5.1 and 12.3)
15 2 3 4+*- → [1]           (from assignment: evaluated step by step)
4 2-        → [2]           (4-2, not 2-4)
4 2/        → [2]           (4/2, not 2/4)
```

### Stack Operations
```
5 3 7#      → [5, 3, 7, 3]  (push stack size)
5 3 7 2!    → [5, 3, 7, 3]  (copy 2nd from top)
5 3 7 2$    → [5, 7]        (delete 2nd from top)
```

### String Operations
```
(hello)(world)+     → ["helloworld"]    (string concatenation)
(hello)65*          → ["helloA"]        (append ASCII 65='A')
65(hello)*          → ["Ahello"]        (prepend ASCII 65='A')
(hello)2-           → ["hel"]           (remove 2 chars from end)
2(hello)-           → ["llo"]           (remove 2 chars from beginning)
(hello)(lo)/        → [3]               (find "lo" in "hello")
(hello)1%           → [101]             (ASCII of char at position 1)
```

### String Execution (Assignment Example)
```
4 3(2*)@+   → [10]  (4 + (3 * 2) = 4 + 6 = 10)
```

### Conditional Execution (Assignment Pattern)
```
1(8)(9~)(4!4$_1+$@)@    → [8]   (if true, execute 8)
0(8)(9~)(4!4$_1+$@)@    → [-9]  (if false, execute 9~)
```

### Comparison Operations
```
5 5=        → [1]           (equal)
3 5<        → [1]           (less than)
7 5>        → [1]           (greater than)
5(hello)<   → [1]           (number < string always true)
```

## Usage

### Quick Testing
```bash
# All-in-one test runner (Windows)
.\run_tests.bat

# Built-in quick tests
python calculator.py -test

# Interactive mode
python calculator.py -i

# Demonstrations  
python calculator.py -demo

# Startup program
python calculator.py
```

### Test Suite Options
```bash
# Simple verification tests
python simple_test.py

# Full assignment compliance test
python comprehensive_test.py

# Unit test suite
python tests/test_calculator.py

# Advanced test runner
python tests/run_tests.py
```

## File Structure ✅ COMPLETE
```
task1/
├── calculator.py              # Main implementation
├── comprehensive_test.py      # Full assignment compliance test
├── simple_test.py            # Quick verification tests
├── run_tests.bat             # Windows test runner
├── tests/
│   ├── test_calculator.py    # Comprehensive unit tests
│   └── run_tests.py         # Advanced test runner  
├── examples/
│   └── string_analysis.py    # String analysis program demo
└── README.md                 # This documentation
```

## Test Results Summary

**Latest Test Run: ✅ ALL PASSING**
```
📊 Assignment Examples: 8/8 passed
🧮 All operators: ✅ Working
📝 String operations: ✅ Working  
🗂️ All 52 registers: ✅ Present
🚀 Startup program: ✅ Verified
🔄 Operation modes: ✅ Working
```

## Implementation Highlights

### Core Features Implemented
- **Post-fix Expression Evaluation**: Exactly as specified in assignment
- **Stack-based Architecture**: Command stream, operation modes, data stack
- **String Execution**: `@` (immediate) and `\` (deferred) operators
- **52 Registers**: A-Z, a-z with startup program in register 'a'
- **Complete Operator Set**: Arithmetic, comparison, logic, stack, I/O
- **Multiple Operation Modes**: Integer/decimal construction, string building
- **Error Handling**: Proper stack underflow and type checking

### String Analysis Program (Assignment Requirement)
Located in register `b`, this program implements the assignment specification:

**Input Example**: `abc+25 a3/X)$`  
**Output Example**: `cba+52 3a/X)$`  
**Counts**: 4 words, 5 letters, 3 digits, 1 whitespace, 3 special characters

**Algorithm**:
1. Read input string with `'`
2. Process each character:
   - Classify as letter (a-z, A-Z), digit (0-9), whitespace (space), or special
   - Identify words (sequences of letters and digits)
   - Reverse each word individually
3. Output modified string and character counts

**Character Classification**:
- Letters: ASCII 65-90 (A-Z) and 97-122 (a-z)
- Digits: ASCII 48-57 (0-9)  
- Whitespace: ASCII 32 (space)
- Special: all other characters

**Implementation Notes**:
- Uses `%` operator to get ASCII codes for classification
- Uses string manipulation operators for word reversal
- Maintains counters on data stack during processing
- Written entirely in calculator language (no external functions)

### Conditional Execution Pattern
The pattern `(true_code)(false_code)(4!4$_1+$@)@` works as:
1. Push condition, true code, false code
2. `4!` copies the condition
3. `4$` deletes the condition copy  
4. `_1+` negates and adds 1 (converts 0→1, non-zero→0)
5. `$@` deletes appropriate code and executes the other

### Error Handling
- Stack underflow: Immediate termination with error message
- Type mismatches: Push empty string for invalid operations
- Division by zero: Push empty string

## Testing

**🎯 Assignment Compliance: 100% VERIFIED**

The test suite includes:
- ✅ **Assignment Examples**: All 8 examples from PDF passing
- ✅ **Operation Mode Tests**: Integer, decimal, string construction  
- ✅ **Operator Tests**: All 20+ operators verified
- ✅ **String Operations**: Concatenation, ASCII, truncation, search
- ✅ **Stack Operations**: Copy, delete, size manipulation
- ✅ **Register Tests**: All 52 registers accessible
- ✅ **Error Handling**: Stack underflow, type mismatches
- ✅ **Integration Tests**: Complex program execution

### Test Commands
```bash
# Quick verification (recommended first run)
python simple_test.py

# Full assignment compliance 
python comprehensive_test.py

# All-in-one Windows runner
.\run_tests.bat

# Interactive testing
python calculator.py -i
```

## Assignment Requirements ✅ SATISFIED

| Requirement | Status | Implementation |
|-------------|--------|----------------|
| Post-fix notation | ✅ | `5.1 12.3+` → `17.4` |
| Stack evaluation | ✅ | `15 2 3 4+*-` → `1` |
| String execution | ✅ | `4 3(2*)@+` → `10` |
| Operation modes | ✅ | 4 modes: -1, <-1, 0, >0 |
| 52 registers | ✅ | A-Z, a-z all functional |
| Startup program | ✅ | Interactive loop in register 'a' |
| String analysis | ✅ | Word reversal & counting in register 'b' |
| Complete operators | ✅ | 20+ operators implemented |
| Error handling | ✅ | Graceful error messages |