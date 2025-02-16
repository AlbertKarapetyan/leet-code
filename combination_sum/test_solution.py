import unittest

from combination_sum import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
     
    def test_combination_sum(self):
        self.assertEqual(self.solution.combination_sum([2,3,5], 8), [[2,2,2,2],[2,3,3],[3,5]])
        self.assertEqual(self.solution.combination_sum([2,3,6,7], 7), [[2,2,3],[7]])
        self.assertEqual(self.solution.combination_sum([2], 1), [])
        self.assertEqual(self.solution.combination_sum([2, 8, 6, 1], 8), [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2], [1, 1, 1, 1, 2, 2], [1, 1, 2, 2, 2], [1, 1, 6], [2, 2, 2, 2], [2, 6], [8]])
        
if __name__ == "__main__":
    unittest.main()