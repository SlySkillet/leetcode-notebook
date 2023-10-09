# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/description/
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = s.split()
        return len(lst[len(lst)-1])
