class Solution:
    symbols = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
        "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900
    }

    def roman_to_int(self, s: str) -> int:
        num, i = 0, 0
        while i < len(s):
            if i < len(s) - 1 and s[i : i + 2] in self.symbols:
                num += self.symbols[s[i : i + 2]]
                i += 2
            else:
                num += self.symbols[s[i]]
                i += 1
            
        return num


obj = Solution()
symbols = "MCMXCIV" 

print(obj.roman_to_int(symbols))