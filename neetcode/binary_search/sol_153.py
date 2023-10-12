# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)- 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < nums[m-1] or r == 0: #finds the pivot point in the array
                return nums[m]
            elif nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1

# neetcode solution with same run time:
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
