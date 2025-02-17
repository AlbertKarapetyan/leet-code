import unittest

from group_anagrams import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
     
    def test_group_anagrams(self):
        self.assertEqual(self.solution.group_anagrams(["eat","tea","tan","ate","nat","bat"]), sorted([["bat"],["nat","tan"],["ate","eat","tea"]]))
        self.assertEqual(self.solution.group_anagrams([""]), [[""]])
        self.assertEqual(self.solution.group_anagrams(["a"]), [["a"]])
       
if __name__ == "__main__":
    unittest.main()