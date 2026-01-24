

from typing import List, Optional, Dict, Set

# Minimize Maximum Pair Sum in Array

# LeetCode: https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums) -1
        result = 0
        while i < j:
            pair_sum = nums[i] + nums[j]
            result = max(result,pair_sum)
            i += 1
            j -= 1
        return result

# --- Driver Code for Local Testing ---

if __name__ == "__main__":
    sol = Solution()
    nums = [3,5,2,3]
    print(sol.minPairSum(nums=nums))

