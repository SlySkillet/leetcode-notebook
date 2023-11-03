# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

# solution with pseudocode
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() #set dummy node as first node in output list
        tail = dummy
        while list1 and list2: #set loop to iterate while their are two lists with values to compare
            if list1.val < list2.val: #check two values against eachother to determine which should push to output list first
                tail.next = list1 # assigns list1node to next value
                list1 = list1.next # creates new head for comparison in next iteration
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next # moves output pointer to next node

        # check if nodes remain in list1 or list2 and pushes them to output
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next # returns all nodes we've linked up except the dummy node
