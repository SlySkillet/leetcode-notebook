# 66. Plus One
# https://leetcode.com/problems/plus-one/description/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        multiplier = 10 ** (len(digits) - 1)
        num = 0
        result = []
        for digit in digits:
            num += digit * multiplier
            multiplier = multiplier / 10
        num += 1
        num = str(num)
        for i in range(len(num)):
            result.append(int(num[i]))
        return result
