# 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needle_size = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+needle_size] == needle:
                return i
        return -1
