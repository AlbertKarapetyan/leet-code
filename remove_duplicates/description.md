# Remove Duplicates from Sorted Array

## Problem Statement  
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`. To get accepted, you need to do the following:

- Change the array `nums` such that the first `k` elements contain the unique elements in the order they were initially present.
- The remaining elements of `nums` are not important.
- Return `k`.

### Custom Judge:
The judge will test your solution with the following code:
```java
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```
If all assertions pass, then your solution will be accepted.

## Examples  

### Example 1  
**Input:**  
```plaintext
nums = [1,1,2]
```  
**Output:**  
```plaintext
2, nums = [1,2,_]
```  
**Explanation:** Your function should return `k = 2`, with the first two elements of `nums` being `1` and `2` respectively. The underscores represent any values left beyond `k` that are not important.

### Example 2  
**Input:**  
```plaintext
nums = [0,0,1,1,1,2,2,3,3,4]
```  
**Output:**  
```plaintext
5, nums = [0,1,2,3,4,_,_,_,_,_]
```  
**Explanation:** Your function should return `k = 5`, with the first five elements of `nums` being `0, 1, 2, 3,` and `4` respectively. The underscores represent any values left beyond `k` that are not important.

## Constraints  
- `1 <= nums.length <= 3 * 10^4`  
- `-100 <= nums[i] <= 100`  
- `nums` is sorted in non-decreasing order.