#!/usr/bin/env python3
"""
Test Runner for Post-fix Calculator
LVA 185.208 Programming Languages - Task 1
"""

import sys
import os
import unittest

# Ensure we can import from the parent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# Now import calculator
try:
    from calculator import Calculator
    print("✓ Calculator module imported successfully")
except ImportError as e:
    print(f"✗ Error importing calculator module: {e}")
    sys.exit(1)

# Define test classes directly here to avoid import issues
class TestAssignmentExamples(unittest.TestCase):
    """Test examples directly from the assignment document"""
    
    def setUp(self):
        """Set up test calculator instance"""
        self.calc = Calculator()
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
    
    def test_string_execution_example(self):
        """Test: 4 3(2*)@+ evaluates to 10 (4 + (3*2))"""
        result = self.execute_and_get_stack("4 3(2*)@+")
        self.assertEqual(result, [10])
    
    def test_conditional_execution_true(self):
        """Test conditional execution from assignment example - true case"""
        result = self.execute_and_get_stack("1(8)(9~)(4!4$_1+$@)@")
        self.assertEqual(result[-1], 8)
    
    def test_conditional_execution_false(self):
        """Test conditional execution from assignment example - false case"""
        result = self.execute_and_get_stack("0(8)(9~)(4!4$_1+$@)@")
        self.assertEqual(result[-1], -9)

class TestArithmeticOperations(unittest.TestCase):
    """Test arithmetic operations according to assignment specification"""
    
    def setUp(self):
        self.calc = Calculator()
        self.calc.command_stream = ""
        self.calc.data_stack.clear()
    
    def execute_and_get_stack(self, commands):
        self.calc.command_stream = commands
        self.calc.run()
        return self.calc.data_stack.copy()
    
    def test_subtraction_order(self):
        """Test that 4 2- gives 2 (not -2)"""
        result = self.execute_and_get_stack("4 2-")
        self.assertEqual(result, [2])
    
    def test_division_order(self):
        """Test that 4 2/ gives 2 (not 0.5)"""
        result = self.execute_and_get_stack("4 2/")
        self.assertEqual(result, [2])
    
    def test_string_concatenation(self):
        """Test string concatenation with +"""
        result = self.execute_and_get_stack("(hello)(world)+")
        self.assertEqual(result, ["helloworld"])
    
    def test_string_ascii_operations(self):
        """Test string operations with ASCII characters"""
        result = self.execute_and_get_stack("(hello)65*")
        self.assertEqual(result, ["helloA"])

class TestStackOperations(unittest.TestCase):
    """Test stack manipulation operations"""
    
    def setUp(self):
        self.calc = Calculator()
        self.calc.command_stream = ""
        self.calc.data_stack.clear()
    
    def execute_and_get_stack(self, commands):
        self.calc.command_stream = commands
        self.calc.run()
        return self.calc.data_stack.copy()
    
    def test_copy_operation(self):
        """Test ! (copy) operation"""
        result = self.execute_and_get_stack("5 3 1!")
        self.assertEqual(result, [5, 3, 3])
        
        self.calc.data_stack.clear()
        result = self.execute_and_get_stack("5 3 7 2!")
        self.assertEqual(result, [5, 3, 7, 3])
    
    def test_delete_operation(self):
        """Test $ (delete) operation"""
        result = self.execute_and_get_stack("5 3 7 1$")
        self.assertEqual(result, [5, 3])
        
        self.calc.data_stack.clear()
        result = self.execute_and_get_stack("5 3 7 2$")
        self.assertEqual(result, [5, 7])
    
    def test_stack_size(self):
        """Test # (stack size) operation"""
        result = self.execute_and_get_stack("5 3 7#")
        self.assertEqual(result, [5, 3, 7, 3])

def run_quick_tests():
    """Run quick verification tests"""
    print("\n" + "="*50)
    print("QUICK VERIFICATION TESTS")
    print("="*50)
    
    calc = Calculator()
    
    tests = [
        ("5.1 12.3+", 17.4, "Basic floating point addition"),
        ("15 2 3 4+*-", 1, "Complex expression evaluation"),
        ("4 3(2*)@+", 10, "String execution"),
        ("4 2-", 2, "Subtraction order"),
        ("4 2/", 2, "Division order"),
        ("(hello)(world)+", "helloworld", "String concatenation"),
        ("(hello)65*", "helloA", "ASCII character insertion"),
        ("5 3 1!", [5, 3, 3], "Stack copy operation"),
    ]
    
    passed = 0
    total = len(tests)
    
    for i, (program, expected, description) in enumerate(tests, 1):
        calc.data_stack.clear()
        calc.command_stream = program
        try:
            calc.run()
            result = calc.data_stack[0] if len(calc.data_stack) == 1 else calc.data_stack.copy()
            
            if isinstance(expected, float):
                success = abs(result - expected) < 0.001
            elif isinstance(expected, list):
                success = result == expected
            else:
                success = result == expected
                
            status = "✓ PASS" if success else "✗ FAIL"
            print(f"{status} Test {i}/{total}: {description}")
            print(f"      {program} = {result}")
            if success:
                passed += 1
            else:
                print(f"      Expected: {expected}")
                
        except Exception as e:
            print(f"✗ FAIL Test {i}/{total}: {description}")
            print(f"      {program} -> Error: {e}")
    
    print(f"\nResults: {passed}/{total} tests passed")
    return passed == total

def run_assignment_verification():
    """Run verification tests based on assignment examples"""
    print("\n" + "="*50)
    print("ASSIGNMENT VERIFICATION TESTS")
    print("="*50)
    
    calc = Calculator()
    
    # Test specific assignment examples
    examples = [
        ("5.1 12.3+", 17.4, "Assignment example: 5.1 + 12.3"),
        ("15 2 3 4+*-", 1, "Assignment example: 15 - (2 * (3 + 4))"),
        ("4 3(2*)@+", 10, "Assignment example: string execution"),
    ]
    
    for program, expected, description in examples:
        calc.data_stack.clear()
        calc.command_stream = program
        calc.run()
        result = calc.data_stack[0]
        
        if isinstance(expected, float):
            success = abs(result - expected) < 0.001
        else:
            success = result == expected
        
        status = "✓ VERIFIED" if success else "✗ FAILED"
        print(f"{status}: {description}")
        print(f"         {program} = {result} (expected {expected})")

def main():
    """Main test runner"""
    print("Task 1: Post-fix Calculator Test Runner")
    print("=" * 50)
    
    # Run quick tests first
    quick_success = run_quick_tests()
    
    # Run assignment verification
    run_assignment_verification()
    
    # Run unit tests
    print("\n" + "="*50)
    print("RUNNING UNIT TESTS")
    print("="*50)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    test_classes = [
        TestAssignmentExamples,
        TestArithmeticOperations,
        TestStackOperations,
    ]
    
    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Summary
    print("\n" + "="*50)
    print("TEST SUMMARY")
    print("="*50)
    print(f"Quick tests: {'✓ PASSED' if quick_success else '✗ FAILED'}")
    print(f"Unit tests: {result.testsRun} run, {len(result.failures)} failures, {len(result.errors)} errors")
    
    if result.failures:
        print("\nFailures:")
        for test, traceback in result.failures:
            print(f"  - {test}: {traceback.split('AssertionError:')[-1].strip()}")
    
    if result.errors:
        print("\nErrors:")
        for test, traceback in result.errors:
            print(f"  - {test}: {traceback.split('\\n')[-2]}")
    
    overall_success = quick_success and len(result.failures) == 0 and len(result.errors) == 0
    print(f"\nOverall: {'✓ ALL TESTS PASSED' if overall_success else '✗ SOME TESTS FAILED'}")

if __name__ == "__main__":
    main()