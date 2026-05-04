

from typing import List, Optional, Dict, Set

# Product of Array Except Self

# LeetCode: https://leetcode.com/problems/product-of-array-except-self/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize list so indices exist
        answer = [1] * n 
        # Storing prefix products directly in answer array 
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]
            
        right = 1 # keeps track of the product to the right
        for i in range(n - 1, -1, -1):
            # Multiply the prefix product by the current right
            answer[i] = answer[i] * right
            # Update right for the next element to the left
            right *= nums[i]
        

        return answer 
# --- Driver Code for Local Testing ---

if __name__ == "__main__":
    sol = Solution()
    result = sol.productExceptSelf(nums=[1,2,3,4])
    print(f"Result: {result}")

