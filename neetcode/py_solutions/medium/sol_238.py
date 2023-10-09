# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/
# initial solution - times out on a large input
from operator import mul
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # create an empty result array
        result = []
        # set a hashmap as a copy of array
        hashmap = list(nums)
        # loop over array
        for i in range(len(nums)):
            # remove index from hashmap
            hashmap.pop(0)
            print(hashmap)
            # calculate sum of hashmap
            hash_product = reduce(mul, hashmap)
            # append sum to result array
            result.append(hash_product)
            print('product', hash_product)
            # put number back in hashmap
            print(nums[i])
            hashmap.append(nums[i])
        return result

# neetcode solution
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

# https://www.youtube.com/watch?v=bNvIQI2wAjk
