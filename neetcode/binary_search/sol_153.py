# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)- 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < nums[m-1] or r == 0:
                return nums[m]
            elif nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1
