# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description/
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxVol = 0
        while l < r:
            diff = r - l
            h = min(height[l], height[r])
            curVol = h * diff
            if curVol > maxVol:
                maxVol = curVol
            if h == height[l]:
                l += 1
            else:
                r -= 1
        return maxVol


solution_instance = Solution()

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
max_area = solution_instance.maxArea(height)

print("maximillian = ", max_area)

import pandas as pd

try:
    pd.__version__
    print("version: ", pd.__version__)
except ImportError:
    print("pandas not  installed")