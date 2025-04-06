import unittest

from remove_duplicates import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
     
    def test_remove_duplicates(self):
        self.assertEqual(self.solution.remove_duplicates([1,1,2]), 2)
        self.assertEqual(self.solution.remove_duplicates([0,0,1,1,1,2,2,3,3,4]), 5)
        
if __name__ == "__main__":
    unittest.main()