# TDD with Python

#### Why should we use TDD?
- TDD is widely used and is the cheapest way to test the code or implement test driven development

#### What are the benefits of TDD?

**Best use cases**
- We will use pytest unittest in Python to implement TDD

```python
def greeting(name):
	return "Hello" + name
```

```python
def thanks(name):
	return "Thank you for visiting," + name
```

- Assertions inherited from unittest TestClass
```    
|Method |   Checks that|   New in |
|:---|:---|:---|
|assertEqual(a, b)        | a == b              ||
|assertNotEqual(a, b)     |    a != b              ||  
|assertTrue(x)            |    bool(x) is True     ||  
|assertFalse(x)           |    bool(x) is False    ||  
|assertIs(a, b)           |    a is b             |3.1|
|assertIsNot(a, b)        |    a is not b          |3.1|
|assertIsNone(x)          |    x is None           |3.1|
|assertIsNotNone(x)       |    x is not None       |3.1|
|assertIn(a, b)           |    a in b              |3.1|
|assertNotIn(a, b)        |    a not in b         |3.1|
|assertIsInstance(a, b)   |    isinstance(a, b)    |3.2|
|assertNotIsInstance(a, b)|    not isinstance(a, b)|3.2| 
```

**Best practices for TDD**
- Write the smallest possible test case that matches what we need to program
* TDD cycle starts with everythong failing - `RED`
* Write code to pass the test - `GREEN`
* Refactor the code for next test - `BLUE`
- And this goes on until all the tests are successfully passed

- Let's create a file called `test_unittest_simplecalc.py`
- Naming convention is extremenly important when it comes to TDD in Python