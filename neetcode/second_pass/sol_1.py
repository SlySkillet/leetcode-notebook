from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} #val: idx
        enums = enumerate(nums) # enumerate nums creates a list of tuples (index, value)
        for idx, num in enums: # iterate over all tuples in the list
            targetInMap = target - num # for each num in nums we're looking for the value, the target in our hashmap, that adds to our target
            if targetInMap in hashMap:
                return [hashMap[targetInMap], idx]
            hashMap[num] = idx # map num: idx (value: index)

solution_instance = Solution()
print(solution_instance.twoSum([2,7,11,15], 9))
