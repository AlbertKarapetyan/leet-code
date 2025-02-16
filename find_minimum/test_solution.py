import unittest

from find_minimum import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
     
    def test_find_min(self):
        self.assertEqual(self.solution.find_min([3,4,5,1,2]), 1)
        self.assertEqual(self.solution.find_min([4,5,6,7,0,1,2]), 0)
        self.assertEqual(self.solution.find_min([11,13,15,17]), 11)
        self.assertEqual(self.solution.find_min([12, 17, 18, 26, 6, 8, 9, 10]), 6)
        
if __name__ == "__main__":
    unittest.main()