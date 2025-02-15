import unittest

from roman_to_int import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
     
    def test_roman_to_int(self):
        self.assertEqual(self.solution.roman_to_int("MCMXCIV"), 1994)
        self.assertEqual(self.solution.roman_to_int("III"), 3)
        self.assertEqual(self.solution.roman_to_int("LVIII"), 58)
        
if __name__ == "__main__":
    unittest.main()