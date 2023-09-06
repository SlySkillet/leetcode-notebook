# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/description/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sorted_s=sorted([ord(n) for n in list(s)])
        sorted_t=sorted([ord(n) for n in list(t)])
        return sorted_s == sorted_t
