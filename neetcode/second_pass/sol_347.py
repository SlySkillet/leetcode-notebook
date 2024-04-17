from typing import List
class Solution():
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        freq = [[]for i in range(len(nums) + 1)]
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        for num, count in hashMap.items():
            freq[count].append(num)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

inst = Solution()
print(inst.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
