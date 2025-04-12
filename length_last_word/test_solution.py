import unittest

from length_of_last_word import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
     
    def test_length_of_last_word(self):
        self.assertEqual(self.solution.length_of_last_word("Hello World"), 5)
        self.assertEqual(self.solution.length_of_last_word("   fly me   to   the moon  "), 4)
        self.assertEqual(self.solution.length_of_last_word("luffy is still joyboy"), 6)
        
if __name__ == "__main__":
    unittest.main()