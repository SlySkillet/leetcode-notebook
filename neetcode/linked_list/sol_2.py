# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur1, cur2 = l1, l2
        res = dummy
        carry = 0
        while cur1 and cur2:
            num = cur1.val + cur2.val
            if carry > 0:
                num += carry
                carry = 0
            if num > 9:
                num -= 10
                carry = 1
            res.next = ListNode(num)
            res = res.next
            cur1 = cur1.next
            cur2 = cur2.next
        if cur1:
            while cur1:
                num = cur1.val
                if carry > 0:
                    num += carry
                    carry = 0
                if num > 9:
                    num -= 10
                    carry = 1
                res.next = ListNode(num)
                res = res.next
                cur1 = cur1.next
        elif cur2:
            while cur2:
                num = cur2.val
                if carry > 0:
                    num += carry
                    carry = 0
                if num > 9:
                    num -= 10
                    carry = 1
                res.next = ListNode(num)
                res = res.next
                cur2 = cur2.next
        if carry > 0:
            res.next = ListNode(carry)
        return dummy.next


# refactored neetcode solution
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            digit = val1 + val2 + carry
            carry = digit // 10
            digit = digit % 10
            cur.next = ListNode(digit)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
