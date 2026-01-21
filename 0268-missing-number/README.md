

# Missing Number

### Goal

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

[Question](https://leetcode.com/problems/missing-number/)

## Approach

I realized that if the array contains numbers from `0` to `n`, I can use the mathematical formula for the sum of a series.

The sum of numbers from `0` to `n` is given by the formula $$n * (n + 1) / 2$$. I calculated this expected sum and then subtracted the actual sum of the elements in the `nums` array. The difference between the expected sum and the actual sum is exactly the missing number. This avoids using a Set or sorting.

## Complexity Analysis

* **Time Complexity:** $$O(N)$$, where $$N$$ is the number of elements. We iterate through the array once to calculate the sum.
* **Space Complexity:** $$O(1)$$, as we only use a few variables for the sums.

## Implementation

```python3
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

```

## Result
![Day21](leetcode-day21.png)