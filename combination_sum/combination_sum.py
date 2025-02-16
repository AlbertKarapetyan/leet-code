from typing import List


class Solution:
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        result: List[List[int]] = []
        candidates.sort()   # Sorting helps optimize pruning in the recursion

        def search(start, tg:int, current: List[int]):
            if tg == 0:
                result.append(current.copy())  # If the target is met, add the combination
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > tg:
                    continue   # Skip numbers greater than the remaining target

                current.append(candidates[i])  # Choose the current number
                search(i, tg-candidates[i], current)   # Recursive call with the reduced target
                current.pop()   # Backtrack to explore other possibilities
        
        search(0, target, [])   # Start the recursive search
        return result

# Example usage
obj = Solution()
candidates = [2, 6, 3, 9, 4]
target = 7

print(obj.combination_sum(candidates, target))