class Solution:
    def search_insert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        
        for i in range(len(nums)):
            if nums[i] > target:
                return i
        else:
            return len(nums)


obj = Solution()
# nums = [1,3,5,6]
# target = 5

# nums = [1,3,5,6]
# target = 2

nums = [1,3,5,6]
target = 7

print(obj.search_insert(nums, target))