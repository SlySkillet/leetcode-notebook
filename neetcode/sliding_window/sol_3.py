# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# initial solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        length = 0
        subStr = ""
        if len(s) > 1:
            while r < len(s):
                if len(subStr) == 0:
                    subStr += s[l]
                if s[r] not in subStr:
                    subStr += s[r]
                    r += 1
                    length = max(length, len(subStr))
                else:
                    length = max(length, len(subStr))
                    subStr = ""
                    l += 1
                    r = l + 1
        elif len(s) == 1:
            length = 1
        return length

# neetcode solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
