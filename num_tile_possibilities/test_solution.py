import unittest

from num_tile_possibilities import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
     
    def test_num_tile_possibilities(self):
        self.assertEqual(self.solution.num_tile_possibilities("ABB"), 8)
        self.assertEqual(self.solution.num_tile_possibilities("AAABBC"), 188)
        self.assertEqual(self.solution.num_tile_possibilities("V"), 1)
        
if __name__ == "__main__":
    unittest.main()