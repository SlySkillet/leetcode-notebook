# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description/

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
