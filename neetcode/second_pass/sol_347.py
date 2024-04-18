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




class Solution2():
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {} # value: count
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1

        buckets = [[]for i in range(len(nums) + 1)]
        for num, count in hashMap.items():
            buckets[count].append(num)

        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    print(res)
                    return res

inst = Solution2()
inst.topKFrequent(nums=[5,5,5,4,4,3], k=2)
