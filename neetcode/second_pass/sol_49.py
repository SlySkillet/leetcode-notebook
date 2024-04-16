from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for s in strs:
            ord_s = [0] * 26
            for char in s:
                ord_char = ord(char) - 97
                ord_s[ord_char] += 1
            ord_s = tuple(ord_s)
            hash_map[ord_s].append(s)
        return list(hash_map.values())

inst = Solution()
print(inst.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

"""Solution Refactored"""

class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for s in strs:
            ord_s = [0] * 26
            for char in s:
                ord_s[ord(char) - ord("a")] += 1
            hash_map[tuple(ord_s)].append(s)
        return hash_map.values()

inst2 = Solution2()
print(inst2.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
