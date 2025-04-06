import unittest

from sub_sets import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
     
    def test_sub_sets(self):
        self.assertEqual(self.solution.sub_sets([1, 2, 3]), [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]])
        self.assertEqual(self.solution.sub_sets([0]), [[], [0]])
        
if __name__ == "__main__":
    unittest.main()