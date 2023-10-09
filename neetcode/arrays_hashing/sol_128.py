# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/description/

# initial solution
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(set(nums))
        print(nums)
        hashmap = {0: 1}
        runcounter = 0
        if len(nums) > 0:
            for i in range(len(nums)-1):
                if nums[i+1] == nums[i] + 1:
                    if runcounter in hashmap.keys():
                        hashmap[runcounter] += 1
                    else: hashmap[runcounter] = 2
                else:
                    runcounter += 1
            print(hashmap)
            runs = sorted(hashmap.values(), reverse=True)
            return runs[0]
        return 0

# neetcode solution
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        longest = 0

        for num in nums:
            # check if num is start of a sequence
            if num - 1 not in nums_set:
                length = 0
                while (num + length) in nums_set:
                    length += 1
                longest = max(longest, length)
        return longest
