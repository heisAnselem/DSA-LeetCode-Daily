

from typing import List, Optional, Dict, Set

# Find the Index of the First Occurrence in a String

# LeetCode: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution: 
    # LeetCode method header here 
    #  eg def example(self, nums: List[int]) -> int:
    def strStr(self, haystack: str, needle: str) -> int:
        i = len(needle)
        j = 0
        while j < len(haystack):
            if needle == haystack[j:j+i]:
                return j
            j+=1
        return -1

# --- Driver Code for Local Testing ---

testcases = {"hello":"ll","sadbutsad":"sad","leetcode":"leeto"}
if __name__ == "__main__":
    sol = Solution()
    # Write the test cases here
    # result = sol.example([1, 2, 3])
    # print(f"Result: {result}")
    result = []
    for haystack,needle in testcases.items():
        result.append(sol.strStr(haystack=haystack,needle=needle))
    print(result)
        

