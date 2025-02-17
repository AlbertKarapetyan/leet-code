import unittest

from max_vowels import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
     
    def test_max_vowels(self):
        self.assertEqual(self.solution.max_vowels("abciiidef", 3), 3)
        self.assertEqual(self.solution.max_vowels("aeiou", 2), 2)
        self.assertEqual(self.solution.max_vowels("leetcode", 3), 2)
        
if __name__ == "__main__":
    unittest.main()