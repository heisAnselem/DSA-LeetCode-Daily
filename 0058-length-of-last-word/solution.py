

from typing import List, Optional, Dict, Set

# Length of Last Word

# LeetCode: https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split() handles multiple spaces and stripping automatically
        words = s.split()
        
        # Return the length of the last word in the list
        return len(words[-1])
# --- Driver Code for Local Testing ---

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLastWord("Hello World I'm Anselem "))