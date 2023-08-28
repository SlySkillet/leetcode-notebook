# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/description/
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)

# binary sort solution
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lower, upper = 0, len(nums)
        while lower < upper:
            mid = (lower+upper)//2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                lower = mid + 1
            else:
                upper = mid
        return lower
