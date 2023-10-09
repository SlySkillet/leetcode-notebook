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

# hashmap solution
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count_s, count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        for char in count_s:
            print(char)
            if count_s[char] != count_t.get(char):
                return False
        return True
