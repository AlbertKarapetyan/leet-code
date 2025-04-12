# 📏 Length of Last Word

Given a string `s` consisting of words and spaces, return the length of the **last word** in the string.

A **word** is defined as a maximal substring consisting of **non-space characters only**.

---

## ✨ Examples

### Example 1:
```python
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```

### Example 2:
```python
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
```

### Example 3:
```python
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
```

---

## 🧩 Constraints
- `1 <= s.length <= 10^4`
- `s` consists of only English letters and spaces `' '`.
- There will be **at least one word** in `s`.

---

## ✅ Tips
To solve this, you can:
- Use `str.strip()` to remove leading/trailing spaces.
- Use `str.split()` to split the string into words.
- Return the length of the last word.

