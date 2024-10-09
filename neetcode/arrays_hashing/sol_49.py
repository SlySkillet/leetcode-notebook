# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/
from collections import defaultdict
#
# ================ NOTE =================
# this import was missing in the original code
# https://docs.python.org/3/library/typing.html
# research typing for a better understanding or a blog post
#
from typing import List

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

#  neetcode solution
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = defaultdict(list) #mapping charCount to list of Anagrams
        for s in strs:
            count = [0] * 26 #a ... z
            for c in s:
                count[ord(c) - ord("a")] += 1

            hashmap[tuple(count)].append(s)

        return hashmap.values()

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hashmap where default value is a list
        hashmap = defaultdict(list)
        # iterate over strs
        for s in strs:
            # create a count variable that is a list of 26 values for each letter of the alphabet. Initial value is 0
            count = [0] * 26
            # iterate over string
            for c in s:
                # take ord of letter, subtract ord('a') to get index of count character and add 1 at that index in the count list
                count[ord(c) - ord('a')] += 1
            # convert count list to a tuple so it is hashable and create a key in hashmap with that tuple and append the string to it
            hashmap[tuple(count)].append(s)
        # return list of hashmap values
        return hashmap.values()
