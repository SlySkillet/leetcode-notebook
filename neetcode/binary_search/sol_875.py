# 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/description/
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        why is it not necessary to sort the input? when we define k we effectively create an array of integers between 1 and the largest pile. Those are the values we perform the binary search on and for each check, it is run against each pile to determine how many hours it takes to eat each pile at rate 'k'
        """
        l, r = 1 , max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res
