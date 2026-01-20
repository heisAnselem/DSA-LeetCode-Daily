

# Path Crossing

### Goal

Given a string `path`, where `path[i] = 'N'`, `'S'`, `'E'` or `'W'`, each representing moving one unit north, south, east, or west, respectively. You start at the origin `(0, 0)` on a 2D plane and walk on the path specified by `path`. Return `true` if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return `false` otherwise.

[Question](https://leetcode.com/problems/path-crossing/)

## Approach

I simulated the movement on a 2D plane by tracking the current coordinates `(x, y)`. I started at `(0, 0)` and maintained a **Hash Set** to store every visited location.

As I iterated through the path string, I updated the `x` or `y` coordinates based on the direction. Before moving to the next step, I checked if the new `(x, y)` tuple already existed in the set. If it did, it meant the path crossed itself, and I returned `True`. If the loop completed without finding a duplicate coordinate, I returned `False`.

## Complexity Analysis

* **Time Complexity:** $$O(N)$$, where $$N$$ is the length of the path string. We iterate through the path exactly once, and set lookups/insertions are $$O(1)$$ on average.
* **Space Complexity:** $$O(N)$$, Since we store each unique coordinate visited in the set.

## Implementation

```python3

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # initialize coordinates at origin
        x,y = 0,0
        # set to store visited coordinates as tuples
        visited = {(x,y)}
        for direction in path:
            if direction == "N":
                # move upward (ie increment y)
                y += 1
            elif direction == "S":
                # move downward
                y -= 1
            elif direction == "E":
                # move forward
                x += 1
            elif direction == "W":
                # move backward
                x -= 1
            # Check if this new coordinate has been visited before
            if (x,y) in visited:
                return True 
            visited.add((x,y))
        return False

```

## Result
![Day20](leetcode-day20.png)

