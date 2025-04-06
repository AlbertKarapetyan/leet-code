from itertools import combinations


class Solution:
    def sub_sets(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        for positions in range(len(nums)+1):
            for indices in combinations(nums, positions):
                result.append(list(indices))
        return result


obj = Solution()

#nums = [1,2,3]
#nums = [3,9]
nums = [3,2,4,1]

print(obj.sub_sets(nums))