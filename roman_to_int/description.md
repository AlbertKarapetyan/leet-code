
# Roman to Integer

## Details
Roman numerals are represented by seven different symbols: `I, V, X, L, C, D, and M`.

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

For example:
- `2` is written as `II`, which is simply `1 + 1`.
- `12` is written as `XII`, which is `X + II`.
- `27` is written as `XXVII`, which is `XX + V + II`.

### Special Cases (Subtractive Notation)
Roman numerals are usually written from largest to smallest, but there are exceptions:
- `I` can be placed before `V` (5) and `X` (10) to make `4` (`IV`) and `9` (`IX`).
- `X` can be placed before `L` (50) and `C` (100) to make `40` (`XL`) and `90` (`XC`).
- `C` can be placed before `D` (500) and `M` (1000) to make `400` (`CD`) and `900` (`CM`).

### Task
Given a Roman numeral as input, convert it to an integer.

## Examples

**Example 1:**
```plaintext
Input: s = "III"
Output: 3
Explanation: III = 3.
```

**Example 2:**
```plaintext
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V = 5, III = 3.
```

- **Example 3:**
```plaintext
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90, and IV = 4.
``` 

## Constraints:
```plaintext
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid Roman numeral in the range [1, 3999].
```