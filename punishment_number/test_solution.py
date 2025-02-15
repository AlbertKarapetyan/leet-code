import unittest

from punishment_number import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
     
    def test_punishment_number(self):
        self.assertEqual(self.solution.punishment_number(1), 1)
        self.assertEqual(self.solution.punishment_number(10), 182)
        self.assertEqual(self.solution.punishment_number(12), 182)
        self.assertEqual(self.solution.punishment_number(37), 1478)
        self.assertEqual(self.solution.punishment_number(50), 3503)
        self.assertEqual(self.solution.punishment_number(1000), 10804657)
        
if __name__ == "__main__":
    unittest.main()