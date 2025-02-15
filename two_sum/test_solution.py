import unittest

from two_sum import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
     
    def test_two_sum(self):
        self.assertEqual(self.solution.two_sum([2,7,11,15], 9), (1, 0))
        self.assertEqual(self.solution.two_sum([3,2,4], 6), (2, 1))
        self.assertEqual(self.solution.two_sum([3,3], 6), (1, 0))
        
if __name__ == "__main__":
    unittest.main()