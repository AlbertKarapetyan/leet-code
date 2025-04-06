class Solution:
    def remove_duplicates(self, nums: list[int]) -> int:
        # Initialize the slow pointer (s) to track the position of unique elements
        s = 0

        # Iterate through the array starting from the second element (fast pointer f)
        for f in range(1, len(nums)):
            # If a new unique element is found (not equal to the previous one)
            if nums[f] != nums[s]:
                s += 1  # Move the slow pointer forward
                nums[s] = nums[f]  # Place the unique element at the correct position

        # The number of unique elements is (s + 1), as 's' is zero-based
        return s + 1


# Create an instance of the Solution class
obj = Solution()

# Example input array with duplicates
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

# Print the number of unique elements after removing duplicates
print(obj.remove_duplicates(nums))  # Output: 5
