class Solution:
    def max_vowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        cnt = 0
        for i in range(k):
            if s[i] in vowels:
                cnt += 1
        max_cnt = cnt

        for i in range(k, len(s)):
            if s[i] in vowels:
                cnt += 1
            if s[i - k] in vowels:
                cnt -= 1
            max_cnt = max(max_cnt, cnt)

        return max_cnt



obj = Solution()

s = "abciiidef"
k = 3

print(obj.max_vowels(s, k))