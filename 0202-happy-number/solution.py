

from typing import List, Optional, Dict, Set

# Happy Number

# LeetCode: https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        
        while n not in visited:
            visited.add(n)
            
            # Calculate sum of squares of digits
            n = sum(int(digit) ** 2 for digit in str(n))
            
            if n == 1:
                return True
                
        return False

# --- Driver Code for Local Testing ---

if __name__ == "__main__":
    sol = Solution()
    # Write the test cases here
    result = sol.isHappy(100)
    print(f"Result: {result}")

