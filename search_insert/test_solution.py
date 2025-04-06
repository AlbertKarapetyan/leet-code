import unittest

from search_insert import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
     
    def test_search_insert(self):
        self.assertEqual(self.solution.search_insert([1,3,5,6], 5), 2)
        self.assertEqual(self.solution.search_insert([1,3,5,6], 7), 4)
        self.assertEqual(self.solution.search_insert([1,3,5,6], 2), 1)
        self.assertEqual(self.solution.search_insert([18,32,53,64,78], 2), 0)
        self.assertEqual(self.solution.search_insert([18,32,53,64,78], 57), 3)
        
if __name__ == "__main__":
    unittest.main()