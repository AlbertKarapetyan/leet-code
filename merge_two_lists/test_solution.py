import unittest

from merge_two_lists import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
     
    def test_merge_two_lists(self):
        self.assertEqual(self.solution.merge_two_lists([1,2,4], [1,3,4]), [1, 1, 2, 3, 4, 4])
        self.assertEqual(self.solution.merge_two_lists([], []), [])
        self.assertEqual(self.solution.merge_two_lists([], [0]), [0])
        self.assertEqual(self.solution.merge_two_lists([3], [0]), [0, 3])
        self.assertEqual(self.solution.merge_two_lists([2,4,8,9], [1,3,4,5,8,9,10]), [1, 2, 3, 4, 4, 5, 8, 8, 9, 9, 10])
        
        
if __name__ == "__main__":
    unittest.main()