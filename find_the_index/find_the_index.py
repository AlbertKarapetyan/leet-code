class MyStr(str):
    def __init__(self, haystack:str):
        super().__init__()
        self.haystack = haystack

    def find_desc(self, sub_str:str) -> int:
        if self.haystack == sub_str:
            return 0
        if len(sub_str) > len(self.haystack):
            return -1
        
        index:int = -1
        s:int = len(sub_str) - 1
        ln = len(self.haystack)
        for i in range(1, ln+1):
            f = ln - i
            if self.haystack[f] != sub_str[s]:
                s = len(sub_str) - 1
                if self.haystack[f] != sub_str[s]:
                    continue
            s -= 1
            if s < 0:
                index = f
                s = len(sub_str) - 1
        return index

    def find(self, sub_str:str) -> int:
        if self.haystack == sub_str:
            return 0
        if len(sub_str) > len(self.haystack):
            return -1
        
        index:int = -1
        s:int = 0
        ln = len(self.haystack)
        for i in range(ln):
            if self.haystack[i] != sub_str[s]:
                s = 0
                if self.haystack[i] == sub_str[s]:
                    s += 1
                    continue
            else:
                s += 1
                if s == len(sub_str):
                    index = i - s + 1
                    break
        if index == -1:
            index = self.find_desc(sub_str)
        return index

        # return self.haystack.find(sub_str)
        # print(sub_str)
        # return 0

class Solution:
    def str_str(self, haystack: str, needle: str) -> int:
        my_str = MyStr(haystack)
        return my_str.find(needle)


obj = Solution()
haystack = "hello"
needle = "ll"
# haystack = "sadbutsad"
# needle = "sad"
# haystack = "leetcode"
# needle = "leeto"

# haystack = "mississippi"
# needle = "issip"

haystack = "ississipissip"
needle = "issip"

# haystack = "aaa"
# needle = "aa"

# haystack = "bbbbababbbaabbba"
# needle = "abb"
print(obj.str_str(haystack, needle))