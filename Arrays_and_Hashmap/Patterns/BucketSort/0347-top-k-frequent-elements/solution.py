

from typing import List, Optional, Dict, Set

# Top K Frequent Elements

# LeetCode: https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        frequency = {} # Integers and frequency of occurrence in nums 
        count =[[] for i in range(len(nums) + 1)] # creates empty bucket arrays the size of nums,index mapped to count of elements appearance by count

        for i,num in enumerate(nums):
            frequency[num] = frequency.get(num,0) + 1

        for num,freq in frequency.items():
            # updating each  bucket by elements with same frequency  
            count[freq].append(num)
        
        # descending accross count to get elements with max frequency first 
        for i in range(len(count)-1,0,-1):
            for elem in count[i]:
                result.append(elem)
            if len(result) == k:
                return result 

# --- Driver Code for Local Testing ---

if __name__ == "__main__":
    sol = Solution()
    result = sol.topKFrequent(nums=[1,1,1,2,2,3],k=2)
    print(f"Result: {result}")

