

from typing import List, Optional, Dict, Set

# Missing Number

# LeetCode: https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        
        return expected_sum - actual_sum


# --- Driver Code for Local Testing ---

if __name__ == "__main__":
    sol = Solution()
    numbers = [[3,0,1],[9,6,4,2,3,5,7,0,1],[0,1]]
    for nums in numbers:
        print(sol.missingNumber(nums=nums))

