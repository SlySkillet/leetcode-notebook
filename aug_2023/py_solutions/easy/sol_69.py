# 69. sqrt(x)
# https://leetcode.com/problems/sqrtx/description/

# Herons Method
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Heron's_method
# times out with large integer input

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        guess = x * .5
        print('x', x)
        print('guess', guess)
        while int(guess**2) != x:
            guess = .5 * (guess + (x / guess))
        return int(guess)

# solution with help
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        lo,hi=0,x
        while True:
            n = lo+(hi-lo)//2
            if n*n <= x <(n+1)*(n+1):
                return n
            elif x < n*n:
                hi=n-1
            else:
                lo=n+1
