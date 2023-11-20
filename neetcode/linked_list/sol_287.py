# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/description/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slw, fst = 0, 0
        while True:
            slw = nums[slw]
            fst = nums[nums[fst]]
            if slw == fst:
                break
        slw2 = 0
        while True:
            slw = nums[slw]
            slw2 = nums[slw2]
            if slw == slw2:
                break

        return slw
