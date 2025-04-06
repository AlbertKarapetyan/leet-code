import unittest

from remove_element import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
     
    def test_remove_element(self):
        self.assertEqual(self.solution.remove_element([3,2,2,3], 3), 2)
        self.assertEqual(self.solution.remove_element([0,1,2,2,3,0,4,2]), 2)
        
if __name__ == "__main__":
    unittest.main()