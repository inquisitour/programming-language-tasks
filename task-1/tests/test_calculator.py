#!/usr/bin/env python3
"""
Assignment-Compliant Test Suite for Post-fix Calculator
LVA 185.208 Programming Languages - Task 1

Tests based on specific examples from assignment document
"""

import unittest
import sys
import os

# Add parent directory to path to import calculator
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from calculator import Calculator
except ImportError:
    print("Error: Cannot import calculator module.")
    print("Make sure calculator.py is in the parent directory.")
    print(f"Current directory: {os.getcwd()}")
    print(f"Looking for calculator.py in: {os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}")
    sys.exit(1)

class TestAssignmentExamples(unittest.TestCase):
    """Test examples directly from the assignment document"""
    
    def setUp(self):
        """Set up test calculator instance"""
        self.calc = Calculator()
        # Clear for testing
        self.calc.command_stream = ""
        self.calc.data_stack.clear()
        self.calc.operation_mode = 0
    
    def execute_and_get_stack(self, commands):
        """Execute commands and return final stack state"""
        self.calc.command_stream = commands
        self.calc.run()
        return self.calc.data_stack.copy()
    
    def test_assignment_example_1(self):
        """Test: 5.1 12.3+ applies + to 5.1 and 12.3, giving 17.4"""
        result = self.execute_and_get_stack("5.1 12.3+")
        self.assertEqual(len(result), 1)
        self.assertAlmostEqual(result[0], 17.4, places=5)
    
    def test_assignment_example_2(self):
        """Test: 15 2 3 4+*- is evaluated to 1"""
        result = self.execute_and_get_stack("15 2 3 4+*-")
        self.assertEqual(result, [1])
        
        # Verify step by step per assignment:
        # Stack: [15, 2, 3, 4] → + → [15, 2, 7] → * → [15, 14] → - → [1]
    
    def test_string_execution_example(self):
        """Test: 4 3(2*)@+ evaluates to 10 (4 + (3*2))"""
        result = self.execute_and_get_stack("4 3(2*)@+")
        self.assertEqual(result, [10])
    
    def test_conditional_execution_true(self):
        """Test conditional execution from assignment example - true case"""
        # From assignment: 1(8)(9~)(4!4$_1+$@)@ should result in 8
        result = self.execute_and_get_stack("1(8)(9~)(4!4$_1+$@)@")
        self.assertEqual(result[-1], 8)
    
    def test_conditional_execution_false(self):
        """Test conditional execution from assignment example - false case"""
        # Test with 0 (false) should execute second string (9~)
        result = self.execute_and_get_stack("0(8)(9~)(4!4$_1+$@)@")
        self.assertEqual(result[-1], -9)

class TestOperationModes(unittest.TestCase):
    """Test operation mode transitions as specified in assignment"""
    
    def setUp(self):
        self.calc = Calculator()
        self.calc.command_stream = ""
        self.calc.data_stack.clear()
        self.calc.operation_mode = 0
    
    def test_integer_construction_mode(self):
        """Test integer construction mode (-1)"""
        # Test building multi-digit integer
        result = self.calc.execute_and_get_stack("123")
        self.assertEqual(result, [123])
        
        # Test transition to decimal
        self.calc.data_stack.clear()
        result = self.calc.execute_and_get_stack("12.34")
        self.assertAlmostEqual(result[0], 12.34, places=5)
    
    def test_string_construction_mode(self):
        """Test string construction mode (>0)"""
        # Test simple string
        result = self.calc.execute_and_get_stack("(hello)")
        self.assertEqual(result, ["hello"])
        
        # Test nested parentheses
        self.calc.data_stack.clear()
        result = self.calc.execute_and_get_stack("(a(b)c)")
        self.assertEqual(result, ["a(b)c"])

class TestArithmeticOperations(unittest.TestCase):
    """Test arithmetic operations according to assignment specification"""
    
    def setUp(self):
        self.calc = Calculator()
        self.calc.command_stream = ""
        self.calc.data_stack.clear()
    
    def test_subtraction_order(self):
        """Test that 4 2- gives 2 (not -2)"""
        result = self.calc.execute_and_get_stack("4 2-")
        self.assertEqual(result, [2])
    
    def test_division_order(self):
        """Test that 4 2/ gives 2 (not 0.5)"""
        result = self.calc.execute_and_get_stack("4 2/")
        self.assertEqual(result, [2])
    
    def test_string_concatenation(self):
        """Test string concatenation with +"""
        result = self.calc.execute_and_get_stack("(hello)(world)+")
        self.assertEqual(result, ["helloworld"])
        
        # Test number to string conversion
        self.calc.data_stack.clear()
        result = self.calc.execute_and_get_stack("(hello)5+")
        self.assertEqual(result, ["hello5"])
    
    def test_string_ascii_operations(self):
        """Test string operations with ASCII characters"""
        # Test * with string and ASCII code
        result = self.calc.execute_and_get_stack("(hello)65*")
        self.assertEqual(result, ["helloA"])
        
        # Test with integer first
        self.calc.data_stack.clear()
        result = self.calc.execute_and_get_stack("65(hello)*")
        self.assertEqual(result, ["Ahello"])
    
    def test_string_truncation(self):
        """Test string truncation with -"""
        # Remove from end
        result = self.calc.execute_and_get_stack("(hello)2-")
        self.assertEqual(result, ["hel"])
        
        # Remove from beginning
        self.calc.data_stack.clear()
        result = self.calc.execute_and_get_stack("2(hello)-")
        self.assertEqual(result, ["llo"])

class TestStackOperations(unittest.TestCase):
    """Test stack manipulation operations"""
    
    def setUp(self):
        self.calc = Calculator()
        self.calc.command_stream = ""
        self.calc.data_stack.clear()
    
    def test_copy_operation(self):
        """Test ! (copy) operation"""
        # Test copying from assignment specification
        result = self.calc.execute_and_get_stack("5 3 1!")
        self.assertEqual(result, [5, 3, 3])  # Copy top element
        
        self.calc.data_stack.clear()
        result = self.calc.execute_and_get_stack("5 3 7 2!")
        self.assertEqual(result, [5, 3, 7, 3])  # Copy 2nd from top
    
    def test_delete_operation(self):
        """Test $ (delete) operation"""
        # Test deleting elements
        result = self.calc.execute_and_get_stack("5 3 7 1$")
        self.assertEqual(result, [5, 3])  # Delete top element
        
        self.calc.data_stack.clear()
        result = self.calc.execute_and_get_stack("5 3 7 2$")
        self.assertEqual(result, [5, 7])  # Delete 2nd from top
    
    def test_stack_size(self):
        """Test # (stack size) operation"""
        result = self.calc.execute_and_get_stack("5 3 7#")
        self.assertEqual(result, [5, 3, 7, 3])

class TestComparisonOperations(unittest.TestCase):
    """Test comparison operations with epsilon handling"""
    
    def setUp(self):
        self.calc = Calculator()
        self.calc.command_stream = ""
        self.calc.data_stack.clear()
    
    def test_integer_comparison(self):
        """Test integer comparisons"""
        result = self.calc.execute_and_get_stack("5 5=")
        self.assertEqual(result, [1])
        
        self.calc.data_stack.clear()
        result = self.calc.execute_and_get_stack("3 5<")
        self.assertEqual(result, [1])
        
        self.calc.data_stack.clear()
        result = self.calc.execute_and_get_stack("7 5>")
        self.assertEqual(result, [1])
    
    def test_string_number_comparison(self):
        """Test string vs number comparison (number < string)"""
        result = self.calc.execute_and_get_stack("5(hello)<")
        self.assertEqual(result, [1])  # 5 < "hello"
        
        self.calc.data_stack.clear()
        result = self.calc.execute_and_get_stack("(hello)5>")
        self.assertEqual(result, [1])  # "hello" > 5

class TestLogicOperations(unittest.TestCase):
    """Test logic operations"""
    
    def setUp(self):
        self.calc = Calculator()
        self.calc.command_stream = ""
        self.calc.data_stack.clear()
    
    def test_and_operation(self):
        """Test & (AND) operation"""
        result = self.calc.execute_and_get_stack("1 1&")
        self.assertEqual(result, [1])
        
        self.calc.data_stack.clear()
        result = self.calc.execute_and_get_stack("1 0&")
        self.assertEqual(result, [0])
    
    def test_or_operation(self):
        """Test | (OR) operation"""
        result = self.calc.execute_and_get_stack("0 1|")
        self.assertEqual(result, [1])
        
        self.calc.data_stack.clear()
        result = self.calc.execute_and_get_stack("0 0|")
        self.assertEqual(result, [0])
    
    def test_null_check(self):
        """Test _ (null check) operation"""
        result = self.calc.execute_and_get_stack("0_")
        self.assertEqual(result, [1])
        
        self.calc.data_stack.clear()
        result = self.calc.execute_and_get_stack("()_")
        self.assertEqual(result, [1])
        
        self.calc.data_stack.clear()
        result = self.calc.execute_and_get_stack("5_")
        self.assertEqual(result, [0])

class TestStringExecutionAndControl(unittest.TestCase):
    """Test string execution and program control"""
    
    def setUp(self):
        self.calc = Calculator()
        self.calc.command_stream = ""
        self.calc.data_stack.clear()
    
    def test_immediate_execution(self):
        """Test @ (apply immediately)"""
        result = self.calc.execute_and_get_stack("5(3+)@")
        self.assertEqual(result, [8])
    
    def test_later_execution(self):
        """Test \\ (apply later)"""
        result = self.calc.execute_and_get_stack("5(3+)\\")
        self.assertEqual(result, [8])

class TestRegisterOperations(unittest.TestCase):
    """Test register access"""
    
    def setUp(self):
        self.calc = Calculator()
        self.calc.command_stream = ""
        self.calc.data_stack.clear()
    
    def test_register_access(self):
        """Test accessing registers A-Z, a-z"""
        # Set a register value
        self.calc.registers['A'] = 42
        result = self.calc.execute_and_get_stack("A")
        self.assertEqual(result, [42])
        
        # Test string register
        self.calc.data_stack.clear()
        self.calc.registers['B'] = "(hello)"
        result = self.calc.execute_and_get_stack("B@")
        self.assertEqual(result, ["hello"])

def run_assignment_verification():
    """Run verification tests based on assignment examples"""
    print("=" * 60)
    print("ASSIGNMENT VERIFICATION TESTS")
    print("=" * 60)
    
    calc = Calculator()
    
    # Test 1: Basic post-fix example
    print("\n1. Testing: 5.1 12.3+ → 17.4")
    calc.data_stack.clear()
    calc.command_stream = "5.1 12.3+"
    calc.run()
    print(f"   Result: {calc.data_stack}")
    assert abs(calc.data_stack[0] - 17.4) < 0.001
    
    # Test 2: Complex evaluation
    print("\n2. Testing: 15 2 3 4+*- → 1")
    calc.data_stack.clear()
    calc.command_stream = "15 2 3 4+*-"
    calc.run()
    print(f"   Result: {calc.data_stack}")
    assert calc.data_stack[0] == 1
    
    # Test 3: String execution
    print("\n3. Testing: 4 3(2*)@+ → 10")
    calc.data_stack.clear()
    calc.command_stream = "4 3(2*)@+"
    calc.run()
    print(f"   Result: {calc.data_stack}")
    assert calc.data_stack[0] == 10
    
    # Test 4: Operation order
    print("\n4. Testing operation order: 4 2- → 2 and 4 2/ → 2")
    calc.data_stack.clear()
    calc.command_stream = "4 2-"
    calc.run()
    print(f"   4 2- = {calc.data_stack}")
    assert calc.data_stack[0] == 2
    
    calc.data_stack.clear()
    calc.command_stream = "4 2/"
    calc.run()
    print(f"   4 2/ = {calc.data_stack}")
    assert calc.data_stack[0] == 2
    
    # Test 5: Conditional execution
    print("\n5. Testing conditional execution")
    calc.data_stack.clear()
    calc.command_stream = "1(8)(9~)(4!4$_1+$@)@"
    calc.run()
    print(f"   True case: {calc.data_stack}")
    assert calc.data_stack[-1] == 8
    
    calc.data_stack.clear()
    calc.command_stream = "0(8)(9~)(4!4$_1+$@)@"
    calc.run()
    print(f"   False case: {calc.data_stack}")
    assert calc.data_stack[-1] == -9
    
    print("\n✓ All assignment examples verified successfully!")

def main():
    """Run all tests"""
    print("Running Assignment-Compliant Calculator Tests...")
    
    # Run unit tests
    unittest.main(argv=[''], exit=False, verbosity=2)
    
    # Run verification tests
    run_assignment_verification()

if __name__ == "__main__":
    main()