@echo off
echo Task 1: Post-fix Calculator Test Runner
echo =====================================

echo.
echo Running quick tests...
python calculator.py -test

echo.
echo Running demonstrations...
python calculator.py -demo

echo.
echo Testing file structure...
if exist calculator.py (
    echo ✓ calculator.py found
) else (
    echo ✗ calculator.py not found
)

if exist tests\test_calculator.py (
    echo ✓ test_calculator.py found
) else (
    echo ✗ test_calculator.py not found
)

echo.
echo To run interactive mode: python calculator.py -i
echo To run individual tests: python tests\run_tests.py
echo.
pause