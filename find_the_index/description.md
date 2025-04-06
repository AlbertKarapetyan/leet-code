# Find the Index of the First Occurrence in a String

This project implements a function to find the index of the first occurrence of a substring (`needle`) within a string (`haystack`).

## Problem Statement

Given two strings `needle` and `haystack`, return the index of the **first occurrence** of `needle` in `haystack`, or `-1` if `needle` is **not** part of `haystack`.

## Examples

### Example 1
**Input:** `haystack = "sadbutsad"`, `needle = "sad"`

**Output:** `0`

**Explanation:**
"sad" occurs at index `0` and `6`.
The first occurrence is at index `0`, so the function returns `0`.

### Example 2
**Input:** `haystack = "leetcode"`, `needle = "leeto"`

**Output:** `-1`

**Explanation:**
"leeto" does not occur in "leetcode", so the function returns `-1`.

## Constraints

- `1 <= haystack.length, needle.length <= 10^4`
- Both `haystack` and `needle` consist of only lowercase English letters.

## Usage
This problem can be solved using built-in string methods, such as `indexOf()` in JavaScript or `find()` in Python, or by implementing string matching algorithms like:
- Knuth-Morris-Pratt (KMP)
- Rabin-Karp
- Naive matching

## License
This project is open-source and available under the MIT License.