# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        num2 = 0
        multiplier = 1
        # while l1.next is not None:
        #     num1 += l1.val * multiplier
        #     multiplier *= 10
        print("l1val", l1.val, "l1next", l1.next)
        print("num1", num1)

# work in progress
