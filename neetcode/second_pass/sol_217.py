from typing import List

"""
Fist solution iterates through the input list once checking if
each value is a key in the hashMap. If not, it creates a key of
the number, assigned to the value of 1. If the number is in the
hashMap keys, there is a duplicate and it returns True. If the
function runs through all values in the input list without finding
a duplicate, there is no duplicate, it returns False.
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                return True
        return False

"""
Same logic but emplying a python set(). This data structure is
still hashable, but is optimized for membership lookups, so it
is perfect for this use case.
"""

class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num not in hashset:
                hashset.add(num)
            else:
                return True
        return False

solution_instance = Solution2()
testCases = [
    [1,2,3,1],
    [1,2,3,4],
    [1,1,1,3,3,4,3,2,4,2]
]

for testCase in testCases:
    res = solution_instance.containsDuplicate(testCase)
    print(res)

"""
A faster refactor of Solution2.
"""

class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
