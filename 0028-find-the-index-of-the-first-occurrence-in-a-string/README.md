

# Find the Index of the First Occurrence in a String

[Question](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

## Approach

The problem asks us to find the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

To solve this, I initialized `i` to the length of `needle` and `j` to `0`.

I then looped through the `haystack` string. For each index `j`, I checked if the substring of `haystack` starting at `j` and having the same length as `needle` matches the `needle` string:

1. **Substring Check:** I used string slicing `haystack[j:j+i]`  (to account for string from index j to j + i ,because  i is just the legnth of the string and j+i gives it direction respect to j) to compare the current window with `needle`.
2. **Return Index:** If they matched, I returned the current index `j`.
3. **Increment:** If no match was found, I incremented `j` to check the next position.

## Complexity Analysis

* **Time Complexity:** $$O(N \cdot M)$$
We traverse the `haystack` of size $$N$$ . In each iteration, the slicing and comparison take $$O(M)$$ time, where $$M$$ is the length of the `needle`.
* **Space Complexity:** $$O(1)$$
We do not use any additional data structures that grow with the input size, aside from the temporary string slices created during comparison.

## Implementation

```python3
 
 class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = len(needle)
        j = 0
        while j < len(haystack):
            if needle == haystack[j:j+i]:
                return j
            j+=1
        return -1
        
```
## Result 
<img width="1366" height="646" alt="leetcode-" src="https://gist.github.com/user-attachments/assets/366067b3-e67a-405c-82de-1a8c4972d50f" />

