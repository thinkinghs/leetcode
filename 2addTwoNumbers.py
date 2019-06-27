# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        result_tail = result
        carry = 0
        p, q = l1, l2
        
        while p != None or q != None:
            x = p.val if p else 0
            y = q.val if q else 0
            carry, out = divmod(x + y + carry, 10)
            
            result_tail.next = ListNode(out)
            result_tail = result_tail.next
            
            p = p.next if p else None
            q = q.next if q else None
        if carry > 0:
            result_tail.next = ListNode(carry)
            
        return result.next
