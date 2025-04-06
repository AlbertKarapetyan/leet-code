class Solution:
    def remove_element(self, nums: list[int], val: int) -> int:
        s = 0

        for f in range(len(nums)):
            if nums[f] != val:
                nums[s] = nums[f]
                s += 1

        return s

obj = Solution()

nums = [3,2,2,3]
val = 3

print(obj.remove_element(nums, val))