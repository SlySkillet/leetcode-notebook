# 155. Min Stack
# https://leetcode.com/problems/min-stack/

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val) # determines if val is the minimum value of the stack at the point that it is pushed to the stack
        self.minStack.append(val)


    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
