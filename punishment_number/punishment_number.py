from itertools import combinations

class Solution:
    def summa(self, str_num: str):
        n = len(str_num)
        for positions in range(1, n):
            for indices in combinations(range(1, n), positions):
                start, sm = 0, 0
                for index in indices:
                    sm += int(str_num[start:index])
                    start = index
                sm += int(str_num[start:])
                yield sm

    def punishment_number(self, n: int) -> int:
        total_sum = 1
        for i in range(2, n+1):
            sq = i * i
            str_nums = str(sq)
           # print(i, str_nums) # for debug log

            if any(i == sm for sm in self.summa(str_nums)):  # Early exit optimization
                total_sum += sq

        return total_sum

obj = Solution()

print(obj.punishment_number(50))



