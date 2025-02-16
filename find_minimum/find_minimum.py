from typing import List


class Solution:
    def find_min(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]

# Example usage
obj = Solution()
nums = [3,4,5,9,0,1,2]

print(obj.find_min(nums))
        