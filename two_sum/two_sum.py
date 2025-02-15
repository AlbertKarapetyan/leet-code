class Solution:
    def two_sum(self, nums: list[int], target: int) -> tuple[int, int]:
        num_map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_map:
                return i, num_map[diff]
            num_map[num] = i

obj = Solution()
nums = [3,3] 
target = 6
print(obj.two_sum(nums, target))