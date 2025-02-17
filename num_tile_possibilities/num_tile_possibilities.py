# Import permutations to generate all possible arrangements of tiles
from itertools import  permutations


class Solution:
    def num_tile_possibilities(self, tiles: str) -> int:
        uniques = set()  # Use a set to store unique sequences (to avoid duplicates)
        
        # Generate permutations of all possible lengths (from 1 to len(tiles))
        for i in range(1, len(tiles)+1):
            for c in permutations(tiles, i): # Generate all possible permutations of length 'i'
                # Add the permutation to the set (duplicates are automatically removed)
                uniques.add(c)
        # Print the set of unique sequences for debugging    
        print(uniques)
        
        return len(uniques) # Return the total count of unique sequences

# Create an instance of the Solution class
obj = Solution()

# Input string containing letter tiles
tiles = "ABB"

# Call the method and print the result
print(obj.num_tile_possibilities(tiles))