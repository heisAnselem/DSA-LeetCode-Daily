# my Automation script to generate my readme template,
# handle leetcode default and tests for the python file .

import os
import sys

# --- CONFIGURATION ---
# matches my specific Gist style
README_TEMPLATE = """

# {title}

[Question](https://leetcode.com/problems/{slug}/)

## Approach

## Complexity Analysis

* **Time Complexity:** $$O(N)$$
* **Space Complexity:** $$O(1)$$
## Implementation

```python3
{code_placeholder}
```

"""

PYTHON_TEMPLATE = """

from typing import List, Optional, Dict, Set

# {title}

# LeetCode: https://leetcode.com/problems/{slug}/

class Solution: 
    # LeetCode method header here 
    #  eg def example(self, nums: List[int]) -> int:
    pass

# --- Driver Code for Local Testing ---

if __name__ == "__main__":
    sol = Solution()
    # Write the test cases here
    # result = sol.example([1, 2, 3])
    # print(f"Result: {{result}}")

"""

def create_problem(id, title):
    # Format folder name: 0028-find-the-index... 
    slug = title.lower().replace(" ", "-") 
    folder_name = f"{str(id).zfill(4)}-{slug}"
    # Create folder
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f" Folder  {folder_name} Created successfully.")
    else:
        print(f"⚠️  Folder {folder_name} already exists.")
    # Create README.md
    readme_path = os.path.join(folder_name, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, "w") as f:
            f.write(README_TEMPLATE.format(title=title, slug=slug, code_placeholder="# Code will be here"))
        print(f" Created README.md")
    # Create solution.py
    python_path = os.path.join(folder_name, "solution.py")
    if not os.path.exists(python_path):
        with open(python_path, "w") as f:
            f.write(PYTHON_TEMPLATE.format(title=title, slug=slug))
        print(f" Created solution.py")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: python create.py [ID] '[Title]'")
        sys.exit(1)
    create_problem(sys.argv[1], sys.argv[2])