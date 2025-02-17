# Maximum Number of Vowels in a Substring of Given Length  

## Problem Statement  
Given a string `s` and an integer `k`, return the maximum number of vowel letters in any substring of `s` with length `k`.  

Vowel letters in English are: `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.  

## Examples  

### Example 1  
**Input:**  
```plaintext
s = "abciiidef", k = 3
```  
**Output:**  
```plaintext
3
```  
**Explanation:** The substring `"iii"` contains 3 vowel letters.  

### Example 2  
**Input:**  
```plaintext
s = "aeiou", k = 2
```  
**Output:**  
```plaintext
2
```  
**Explanation:** Any substring of length 2 contains exactly 2 vowels.  

### Example 3  
**Input:**  
```plaintext
s = "leetcode", k = 3
```  
**Output:**  
```plaintext
2
```  
**Explanation:** The substrings `"lee"`, `"eet"`, and `"ode"` contain 2 vowels.  

## Constraints  
- `1 <= s.length <= 10^5`  
- `s` consists of lowercase English letters.  
- `1 <= k <= s.length`