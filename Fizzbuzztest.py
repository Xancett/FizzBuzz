from Fizzbuzz import *
import unittest

class TestFizzbuzz(unittest.TestCase):

	def test_one(self):
		self.assertEqual("1", FizzBuzz(1))
	
	def test_two(self):
		self.assertEqual(["1", "2"], FizzBuzz(2))
	
	def test_three(self):
		self.assertEqual(["1", "2", "Fizz"], FizzBuzz(3))
	
	def test_six(self):
		self.assertEqual(["1", "2", "Fizz", "4", "Buzz", "Fizz"], FizzBuzz(6))
	
	def test_fifteen(self):
		self.assertEqual(["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"], FizzBuzz(15))

if __name__ == "__main__":
	unittest.main()