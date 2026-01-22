# Length of Last Word

### Goal

Given a string `s` consisting of words and spaces, return the length of the **last** word in the string. A word is a maximal substring consisting of non-space characters only.

[Question](https://leetcode.com/problems/length-of-last-word/)

## Approach

I realized that the input string could contain trailing spaces (e.g., `"Hello World  "`). Therefore, I couldn't just check the end of the string directly.

I decided to use Python's built-in string methods to handle the whitespace. By using `.split()`, Python automatically removes leading and trailing whitespace and splits the string by spaces into a list of words. Once I had the clean list of words, I simply accessed the last element (index `-1`) and returned its length.

## Complexity Analysis

* **Time Complexity:** $$O(N)$$, where $$N$$ is the length of the string. The split operation traverses the string once.
* **Space Complexity:** $$O(N)$$, as we create a list of words to store the split parts of the string.

## Implementation

```python3
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split() handles multiple spaces and stripping automatically
        words = s.split()
        
        # Return the length of the last word in the list
        return len(words[-1])

```