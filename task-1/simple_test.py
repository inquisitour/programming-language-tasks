#!/usr/bin/env python3
"""
Simple Test Launcher for Post-fix Calculator
Place this file in the same directory as calculator.py
"""

import sys
import os

def test_calculator():
    """Simple test function that imports and tests calculator"""
    
    print("Task 1: Post-fix Calculator - Simple Tests")
    print("=" * 50)
    
    # Try to import calculator
    try:
        from calculator import Calculator
        print("✓ Calculator imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import calculator: {e}")
        print("\nMake sure this file is in the same directory as calculator.py")
        return False
    
    # Run basic tests
    calc = Calculator()
    
    print("\nRunning basic tests...")
    
    # Test 1: Assignment example 1
    print("\n1. Testing: 5.1 12.3+ → 17.4")
    calc.data_stack.clear()
    calc.command_stream = "5.1 12.3+"
    try:
        calc.run()
        result = calc.data_stack[0] if calc.data_stack else None
        expected = 17.4
        success = abs(result - expected) < 0.001
        print(f"   Result: {result}")
        print(f"   {'✓ PASS' if success else '✗ FAIL'}")
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
    
    # Test 2: Assignment example 2
    print("\n2. Testing: 15 2 3 4+*- → 1")
    calc.data_stack.clear()
    calc.command_stream = "15 2 3 4+*-"
    try:
        calc.run()
        result = calc.data_stack[0] if calc.data_stack else None
        expected = 1
        success = result == expected
        print(f"   Result: {result}")
        print(f"   {'✓ PASS' if success else '✗ FAIL'}")
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
    
    # Test 3: String execution
    print("\n3. Testing: 4 3(2*)@+ → 10")
    calc.data_stack.clear()
    calc.command_stream = "4 3(2*)@+"
    try:
        calc.run()
        result = calc.data_stack[0] if calc.data_stack else None
        expected = 10
        success = result == expected
        print(f"   Result: {result}")
        print(f"   {'✓ PASS' if success else '✗ FAIL'}")
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
    
    # Test 4: Operation order
    print("\n4. Testing: 4 2- → 2 (operation order)")
    calc.data_stack.clear()
    calc.command_stream = "4 2-"
    try:
        calc.run()
        result = calc.data_stack[0] if calc.data_stack else None
        expected = 2
        success = result == expected
        print(f"   Result: {result}")
        print(f"   {'✓ PASS' if success else '✗ FAIL'}")
        if not success:
            print(f"   Expected: {expected} (4-2, not 2-4)")
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
    
    # Test 5: String operations
    print("\n5. Testing: (hello)(world)+ → 'helloworld'")
    calc.data_stack.clear()
    calc.command_stream = "(hello)(world)+"
    try:
        calc.run()
        result = calc.data_stack[0] if calc.data_stack else None
        expected = "helloworld"
        success = result == expected
        print(f"   Result: '{result}'")
        print(f"   {'✓ PASS' if success else '✗ FAIL'}")
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
    
    # Test 6: Stack operations
    print("\n6. Testing: 5 3 7 2! → [5, 3, 7, 3] (copy operation)")
    calc.data_stack.clear()
    calc.command_stream = "5 3 7 2!"
    try:
        calc.run()
        result = calc.data_stack.copy()
        expected = [5, 3, 7, 3]
        success = result == expected
        print(f"   Result: {result}")
        print(f"   {'✓ PASS' if success else '✗ FAIL'}")
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
    
    # Test 7: Conditional execution
    print("\n7. Testing: 1(8)(9~)(4!4$_1+$@)@ → 8 (conditional true)")
    calc.data_stack.clear()
    calc.command_stream = "1(8)(9~)(4!4$_1+$@)@"
    try:
        calc.run()
        result = calc.data_stack[-1] if calc.data_stack else None
        expected = 8
        success = result == expected
        print(f"   Stack after execution: {calc.data_stack}")
        print(f"   Result: {result}")
        print(f"   {'✓ PASS' if success else '✗ FAIL'}")
        if not success and calc.data_stack:
            print(f"   Note: Full stack is {calc.data_stack}, last element is {calc.data_stack[-1]}")
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
    
    # Test 7b: Simpler conditional test
    print("\n7b. Testing simpler conditional: 1(42)@")
    calc.data_stack.clear()
    calc.command_stream = "1(42)@"
    try:
        calc.run()
        result = calc.data_stack[-1] if calc.data_stack else None
        print(f"   Stack: {calc.data_stack}")
        print(f"   Result: {result}")
        print(f"   {'✓ PASS' if result == 42 else '✗ FAIL'}")
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
    
    print("\n" + "=" * 50)
    print("Basic tests completed!")
    print("For interactive testing, run: python calculator.py -i")
    return True

def show_usage():
    """Show usage information"""
    print("""
Usage Options:
==============

1. Run this simple test:
   python simple_test.py

2. Run calculator tests:
   python calculator.py -test

3. Run calculator demos:
   python calculator.py -demo

4. Interactive mode:
   python calculator.py -i

5. Run startup program:
   python calculator.py

File Structure:
===============
Make sure you have:
  calculator.py          (main implementation)
  simple_test.py         (this file)
  tests/test_calculator.py   (full test suite)
  tests/run_tests.py     (test runner)
""")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help', 'help']:
        show_usage()
    else:
        test_calculator()