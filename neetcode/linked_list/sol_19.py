#19. Remove Nth Node from End of List
#https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# initial solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        l = dummy
        r = dummy
        while n >= 0:
            r = r.next
            n -= 1

        while r:
            l = l.next
            r = r.next

        l.next = l.next.next

        return dummy.next

# alt solution - same logic, different writing. For some reason, this alg is running slower on leetcode.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l, r = dummy, head
        while n > 0 and r:
            r = r.next
            n -= 1

        while r:
            l, r = l.next, r.next

        l.next = l.next.next

        return dummy.next
