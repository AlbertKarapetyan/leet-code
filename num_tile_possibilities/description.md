# Letter Tile Possibilities

## Problem Statement  
You have `n` tiles, where each tile has one letter `tiles[i]` printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

## Examples  

### Example 1  
**Input:**  
```plaintext
tiles = "AAB"
```  
**Output:**  
```plaintext
8
```  
**Explanation:** The possible sequences are `"A"`, `"B"`, `"AA"`, `"AB"`, `"BA"`, `"AAB"`, `"ABA"`, `"BAA"`.  

### Example 2  
**Input:**  
```plaintext
tiles = "AAABBC"
```  
**Output:**  
```plaintext
188
```  

### Example 3  
**Input:**  
```plaintext
tiles = "V"
```  
**Output:**  
```plaintext
1
```  

## Constraints  
- `1 <= tiles.length <= 7`  
- `tiles` consists of uppercase English letters.