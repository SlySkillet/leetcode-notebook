# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        result = []
        for i in range(len(strs)):
            ord_str = str(sorted([ord(n) for n in list(strs[i])]))
            if ord_str not in hashmap:
                hashmap[ord_str] = [strs[i]]
            else: hashmap[ord_str].append(strs[i])
        for key in hashmap:
            result.append(hashmap[key])
        return result
