import unittest

from find_the_index import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
     
    def test_find_the_index(self):
        self.assertEqual(self.solution.str_str("sadbutsad", "sad"), 0)
        self.assertEqual(self.solution.str_str("leetcode", "leeto"), -1)
        
if __name__ == "__main__":
    unittest.main()