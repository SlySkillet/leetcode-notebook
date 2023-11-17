# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashMap = {} #node: pos
        point = head
        pos = 0
        while point:
            if point in hashMap:
                return True
            hashMap[point] = pos
            point = point.next
            pos += 1

        return False
