

# Product of Array Except Self

## [Question](https://leetcode.com/problems/product-of-array-except-self) 

Given an integer array `nums`, return _an array_ `answer` _such that_ `answer[i]` _is equal to the product of all the elements of_ `nums` _except_ `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed**to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

**Example 1:**

**Input:** nums = [1,2,3,4]
**Output:** [24,12,8,6]

**Example 2:**

**Input:** nums = [-1,1,0,-3,3]
**Output:** [0,0,9,0,0]

**Constraints:**

- `2 <= nums.length <= 105`
- `-30 <= nums[i] <= 30`
- The input is generated such that `answer[i]` is **guaranteed** to fit in a **32-bit** integer.

**Follow up:** Can you solve the problem in `O(1)` extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)


## Approach 

Initially what came to my mind after reading the question was to use brute force 


Here I can loop through the array `nums` using a pointer `j` for every index `i`, multiply together all the elements at index `j` except when `i = j ` ensuring I prevent  the  element at index `i` from being multiplied 

**Time complexity :** For this solution a time complexity of $O(n^2 )$ is acheived as I use a nested loop each of which runs $n$ times .
**Space complexity :** $O(1)$ exception of the `answer`  array

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]*n
        for i in range(n):
            product = 1 # product tracker 
            for j in range(n):
                if i == j :
                     continue
                # multiplies all elements at index j that are not at index i  
                product *= nums[j]
            # compute answer for each index i
            answer[i] = product  
                
        return answer

But I needed to optimize and see it can be solved in lesser time  , also the question said the algorithm should run in $O(n)$ time ✨ . 

So I thought that I could use two arrays  `prefix` and `suffix`, `prefix` stores the product of the values before that particular index `i` and `suffix` stores the product of the values after it . 
In idea We are essentially splitting the array at the point of the index `i` , hence for every index `i` , `answer [i] = prefix[i] x suffix[i]` 

How do we achieve this ? 🙂

We initially prefill the arrays of size $n$ `prefix, suffix and answer ` with 1  to ensure it can be indexed .
We then transverse from the left to the index `i` of `nums` to fill `prefix` and we transverse from right to the index `i` of `nums` to fill `suffix` .

This way each element excludes itself but includes every other element.

**Time complexity :** For this solution a time complexity of $O(n)$ is achieved since we only iterate once on the `nums` array 
**Space complexity :** $O(n)$ , we make use of arrays that store n values. exception of the `answer`  array

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize lists so indices exist
        prefix = [1] * n
        suffix = [1] * n
        answer = [1] * n 
        
        # Calculate products of all elements to the left of each element
        for i in range(1,n):
            # starting from the second index
            prefix[i] = prefix[i - 1] * nums[i-1]
            
        # Calculate products of all elements to the right of each element
        for i in range(n-2,-1,-1):
            # starting from the penultimate index 
            suffix[i] = suffix[i+1] * nums[i+1]
            
        # Multiply left and right products to get the final result
        for i in range(n):
            answer[i] = prefix[i] * suffix[i]

        return answer 
```

 To further optimize our solution the question asks if I can solve it in $O(1)$ space time complexity 

Thinking about this I could actually do this by storing the prefix products in the `answer` array first, then multiplying the suffix values into it as we go , also updating a variable that keeps track of the suffix values to the right.

Now we have our best solution with $O(1)$  space achieved ✨.

```python
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
         
```

