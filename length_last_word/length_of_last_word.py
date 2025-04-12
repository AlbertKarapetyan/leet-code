class Solution:
    def length_of_last_word(self, s: str) -> int:
        words = s.strip().replace("  "," ").rsplit(" ", 1)
        if len(words) > 1:
            return len(words[1])
        else:
            return len(words[0])


obj = Solution()

s = "Hello World"

print(obj.length_of_last_word(s))