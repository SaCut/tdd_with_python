from bakery_section import Factory
import unittest

bread_quality = "good"

class BreadTest(unittest.TestCase):

	grandma = Factory()
	
	def test_bread(self):
		self.assertTrue(self.grandma.run_factory(bread_quality))