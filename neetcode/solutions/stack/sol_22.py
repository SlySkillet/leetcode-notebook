# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [] # create empty stack
        res = [] # create result list (this will hold valid results when we reach them)
        def backtrack(openN, closedN): # recursive function taking in number of open parentheses and closed parentheses
            if openN == closedN == n: # base case - we have the correct number of parentheses, open and closed are equal
                res.append("".join(stack)) # creates a string from the stack
                return # exit backtrack

            if openN < n: # checks open against n
                stack.append("(") # adds an open
                backtrack(openN + 1, closedN) # calls backtrack with updated count. Now backtrack runs again with an unchanged stack
                stack.pop() # clean up the stack so it is ready for another input when we exit this instance

            if closedN < openN: # check closed against open
                stack.append(")") # append closed to the stack
                backtrack(openN, closedN + 1) # run backtrack on the
                stack.pop() # clean up the stack so it is ready for another input

        backtrack(0,0)
        return res
