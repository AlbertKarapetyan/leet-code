# Group Anagrams

## Problem Statement  
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

## Examples  

### Example 1  
**Input:**  
```plaintext
strs = ["eat","tea","tan","ate","nat","bat"]
```  
**Output:**  
```plaintext
[["bat"],["nat","tan"],["ate","eat","tea"]]
```  
**Explanation:**  
- There is no string in `strs` that can be rearranged to form "bat".
- The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
- The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

### Example 2  
**Input:**  
```plaintext
strs = [""]
```  
**Output:**  
```plaintext
[[""]]
```  

### Example 3  
**Input:**  
```plaintext
strs = ["a"]
```  
**Output:**  
```plaintext
[["a"]]
```  

## Constraints  
- `1 <= strs.length <= 10^4`  
- `0 <= strs[i].length <= 100`  
- `strs[i]` consists of lowercase English letters.