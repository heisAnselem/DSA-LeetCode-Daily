

from typing import List, Optional, Dict, Set

# Reverse String

# LeetCode: https://leetcode.com/problems/reverse-string/

class Solution: 
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        """
        i = 0 # left pointer 
        j = len(s) - 1  # right pointer 

        # Continue looping as long as the left pointer is to the left of the right pointer.
        while i < j:
            # This swaps the values at index i and index j simultaneously.
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1

# --- Driver Code for Local Testing ---

if __name__ == "__main__":
    solution = Solution()
    # Test Case 1
    s1 = ["h","e","l","l","o"]
    solution.reverseString(s1)
    print(f"Test Case 1: {s1}") # Expected: ['o', 'l', 'l', 'e', 'h']

    # Test Case 2
    s2 = ["H","a","n","n","a","h"]
    solution.reverseString(s2)
    print(f"Test Case 2: {s2}") # Expected: ['h', 'a', 'n', 'n', 'a', 'H']


