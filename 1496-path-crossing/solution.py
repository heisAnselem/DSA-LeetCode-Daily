

from typing import List, Optional, Dict, Set

# Path Crossing

# LeetCode: https://leetcode.com/problems/path-crossing/

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

# --- Driver Code for Local Testing ---

if __name__ == "__main__":
    sol = Solution()
    tests = ["NS","NSEWW","NW"]
    expected = [True,True,False]
    result = []
    for path in tests:
        result.append(sol.isPathCrossing(path=path))
    if result == expected:
        print("Correct Solution")
    else:
        print("Wrong Solution")


