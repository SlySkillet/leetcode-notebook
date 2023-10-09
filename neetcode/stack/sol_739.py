# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/description/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #create an empty stack
        ans = [0] * len(temperatures) # create a result list where 0 is the default value for all indexes of temperatures
        for i, t in enumerate(temperatures): # iterate over the index and temps in temperatures
            while stack and stack[-1][1] > t: # check the temp against the top of the stack, if it's greater, we know we have found a warmer day than the top of the stack
                stack_i, stack_t = stack.pop() # we determine the index of that day
                ans[stack_i] = (i - stack_i) # we determine the difference in days (index) and set the index of the day in question (top of the stack) in ans to that difference
            stack.append([i,t]) # add the value from the loop to the stack
        return ans
