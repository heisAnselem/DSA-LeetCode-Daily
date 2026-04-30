

# Top K Frequent Elements

[Question](https://leetcode.com/problems/top-k-frequent-elements/)

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.


## Approach
I reasoned that i could use a hashmap to count the frequency of each elements in the array `nums` where each elements are stored as the keys and their frequency as values .
With this 
My initial approach was to create a hashmap that counts the frequency of each elements in the array `nums` where each elements are stored as the keys and their frequency as values .
We loop through the array and check if each element exists in the hashmap. If it does, we increment its value by 1. If not, we add it to the hashmap with a value of 1.

At this point I was stuck — how do I select the Kth most frequent element?

After checking online,Neetcode and discussions I learned about bucket sort.
We create an array of arrays (buckets), where each index maps to a frequency count. The array length is the max possible frequency (length of input array + 1). Each inner array (bucket) stores all elements that share that frequency.
We then iterate through our hashmap, and for each element, use its frequency to determine which bucket it belongs in.
Finally, we loop from the end of the bucket array to the beginning (since the highest frequencies are at the end), and keep adding elements to our result array until it reaches size K.


## Complexity Analysis

* **Time Complexity:** The overall time complexity is $$O(N)$$ because populating the bucket involves iterating through the hashmap which has at most `n` elements and buildingthefrequency hashmap requires iterating through the nums array once which has also has `n` elements 
* **Space Complexity:** The overall space complexity is $$O(N)$$ also since the hashmap can store at most `n` key-value pairs and the the bucket array across all buckets hold at most `n` elements 
## Implementation

```python3

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
                
```

