# 1. two sum
# https://leetcode.com/problems/two-sum/
# solution explanation https://neetcode.io/practice

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {} # val: index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hash_map:
                return [hash_map[diff], i]
            hash_map[n] = i
