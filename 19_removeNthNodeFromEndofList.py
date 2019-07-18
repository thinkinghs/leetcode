'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n) -> ListNode:
        
        current = head
        length = 0
        
        # current None이면 stop
        while current:
            length += 1
            current = current.next
        
        # idx는 0부터 count
        idx = length - n

        cnt = 0
        result = ListNode(0)
        result_tail = result
        removeCurrent = head
        
        while removeCurrent != None:
            if cnt == idx:
                removeCurrent = removeCurrent.next
                cnt += 1
                continue
            cnt += 1
            result_tail.next = ListNode(removeCurrent.val)
            result_tail = result_tail.next
            removeCurrent = removeCurrent.next
        
        return result.next
