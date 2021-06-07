import unittest
import reverser

class testReverser(unittest.TestCase):

	def test_rev(self):
		self.assertEqual(reverser.rev("Reverse this please"), "please this Reverse")

	def test_rev_1(self):
		self.assertEqual(reverser.rev("23 34 45892 093245"), "093245 45892 34 23")

	def test_rev_2(self):
		self.assertEqual(reverser.rev("Does splicing work?" + 'H'), "work?H splicing Does")


if __name__ == '__main__':
	unittest.main()
