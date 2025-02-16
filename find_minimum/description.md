# Find Minimum in Rotated Sorted Array

## Problem Statement
Suppose an array of length n sorted in ascending order is rotated between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

`[4,5,6,7,0,1,2]` if it was rotated `4` times.
`[0,1,2,4,5,6,7]` if it was rotated `7` times.
Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` `1` time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

### Goal
Implement an algorithm to return the minimum element of `nums` in **O(log n)** time complexity.

## Examples
### Example 1
**Input:** `nums = [3,4,5,1,2]`
**Output:** `1`

**Explanation:**  
The original array was `[1,2,3,4,5]`, rotated 3 times.

### Example 2
**Input:** `nums = [4,5,6,7,0,1,2]`
**Output:** `0`

**Explanation:**  
The original array was `[0,1,2,4,5,6,7]`, rotated 4 times.

### Example 3
**Input:** `nums = [11,13,15,17]`
**Output:** `11`

**Explanation:**  
The original array was `[11,13,15,17]`, rotated 4 times.

## Constraints
- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All elements of `nums` are **unique**.
- `nums` is sorted and rotated between `1` and `n` times.

## Approach
Since the array is sorted but rotated, we can use a **binary search** approach to find the minimum element in **O(log n)** time:
1. Use two pointers (`left` and `right`) to perform a modified binary search.
2. Check the middle element:
   - If `nums[mid] > nums[right]`, the minimum is in the right half.
   - Otherwise, it is in the left half.
3. Continue narrowing the search range until the minimum element is found.

This ensures an efficient logarithmic time complexity solution.

---
This problem is a common example of searching in a **rotated sorted array**, a key concept in algorithmic problem-solving.