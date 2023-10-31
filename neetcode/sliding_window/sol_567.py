# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/description/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = {}
        for char in s1:
            s1Map[char] = s1Map.get(char, 0) + 1
        s2Map = {}
        l, r = 0, len(s1)
        while r <= len(s2):
            for i in range(l, r):
                s2Map[s2[i]] = s2Map.get(s2[i], 0) + 1
            if s1Map == s2Map:
                return True
            print(s1Map, s2Map)
            s2Map = {}
            r += 1
            l += 1
        return False
