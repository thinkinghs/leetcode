# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# easy
# Given a sorted linked list, delete all duplicates such that each element appear only once.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if not head:
            return head
        
        curr = head
        
        while curr.next:
            
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head
