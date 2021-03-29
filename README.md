# TDD Test Driven Development
## Why should we use TDD
### what are the benefits of using TDD

**Best Use Cases** 
- We will use Pytest unittest in Python to implement TDD
- TDD is widely used and is the cheapest way to test the code or implement test driven development 

**Best practices for TDD**
- Write the smallest possible test case that matches what we need program
- TDD cycle start with everything failing - `RED`
- Write code to pass the test `GREEN`
- Refactor the code for next test `BLUE`
- This continues until all the test have successfully passed 

- ![img](https://github.com/SaCut/tdd_with_python/blob/main/TDD_structure.jpg?raw=true)

There are also numerous assertions that are inherited from the TestCase base class, assertions are everything in testing...

|Method |	Checks that|	New in |
|:---|:---|:---|
|assertEqual(a, b)        | a == b              ||
|assertNotEqual(a, b)     |	a != b              ||	 
|assertTrue(x)            |	bool(x) is True     ||	 
|assertFalse(x)           |	bool(x) is False    ||	 
|assertIs(a, b)           |	a is b	            |3.1|
|assertIsNot(a, b)        |	a is not b          |3.1|
|assertIsNone(x)          |	x is None           |3.1|
|assertIsNotNone(x)       |	x is not None       |3.1|
|assertIn(a, b)           |	a in b              |3.1|
|assertNotIn(a, b)        |	a not in b	        |3.1|
|assertIsInstance(a, b)   |	isinstance(a, b)    |3.2|
|assertNotIsInstance(a, b)|	not isinstance(a, b)|3.2| 

- Let's create file called `test_unittest_simplecalc.py`
- Naming convention is extremely important when it comes to TDD in Python
```python
# Let's create tests to check if the code would be running without any errors

from simple_calc import SimpleCalc
# importing the file and class where we would write our code

import unittest
# importing unittest to inherit TestCase to create our tests against the code

class CalcTest(unittest.TestCase):

    calc = SimpleCalc() # creating an object of our SimpleCalc() class

    def test_add(self): #Naming convention - using `test` in the name of our function will let python interpret know that this needs to be tested
        self.assertEqual(self.calc.add(2, 4), 6)
         # this test is checking if 2 + 4 = 6 that would be true, if true test will pass

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)
        # This tests the values as 4 - 2 = 2 to be True if True the test passes

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)
        # This tests the values 2 * 2 = 4 if True the test passes

    def test_divide(self):
        self.assertEqual(self.calc.divide(15, 3), 5)
        # This test 15 / 3 = 5 if true the test passes
```
- Run the tests `python -m pytest`
**Let's write our code now to pass the tests**
```python
class SimpleCalc:
    #  pass
    def add(self, value1, value2):
        return value1 + value2
        # this function adds the values for value1 and value 2 against the test we have in other class

    def subtract(self, value1, value2):
        return value1 - value2

    def multiply(self, value1, value2):
        return value1 * value2

    def divide(self, value1, value2):
        return value1 / value2
```

- Running the test with `python3 -m unittest discover -v`, output:
```
test_add (test_unittest_simplecalc.SimpleTest) ... ok
test_divide (test_unittest_simplecalc.SimpleTest) ... ok
test_multiply (test_unittest_simplecalc.SimpleTest) ... ok
test_subtract (test_unittest_simplecalc.SimpleTest) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s
```
- or with `python3 -m pytest -v`:
```
======================================================== test session starts ========================================================
platform linux -- Python 3.8.5, pytest-6.2.2, py-1.10.0, pluggy-0.13.1 -- /home/saverio/Projects/sparta_global/eng84/bin/python3
cachedir: .pytest_cache
rootdir: /home/saverio/Projects/sparta_global/tdd_with_python
collected 4 items                                                                                                                   

test_unittest_simplecalc.py::SimpleTest::test_add PASSED                [ 25%]
test_unittest_simplecalc.py::SimpleTest::test_divide PASSED             [ 50%]
test_unittest_simplecalc.py::SimpleTest::test_multiply PASSED           [ 75%]
test_unittest_simplecalc.py::SimpleTest::test_subtract PASSED           [100%]

========================= 4 passed in 0.04s =========================
```

#### Summary
- TDD helps reduce unexpected errors
