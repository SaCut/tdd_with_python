# let's create a few test to see if the code runs without any errors

# importing the file and class where we would write our code
from simple_calc import SimpleCalc

# import unittest to inherit TestCase
import unittest

class SimpleTest(unittest.TestCase):

	calc = SimpleCalc() # create an object of our class

	def test_add(self): # naming convention - using 'test' in the name of your function
						# will let the interpreter know that this needs to be tested
		self.assertEqual(self.calc.add(2, 4), 6)
	# this test is checking if 2

	def test_subtract(self):
		self.assertEqual(self.calc.subtract(4, 2), 2)
		# if true the test passes

	def test_multiply(self):
		self.assertEqual(self.calc.multiply(2, 2), 4)
		# this thest assesses if 2 * 2 = 4

	def test_divide(self):
		self.assertEqual(self.calc.divide(12, 3), 4)

# pytest looks for any file with name including 'test*.py'
