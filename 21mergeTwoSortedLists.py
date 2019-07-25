# https://leetcode.com/problems/merge-two-sorted-lists/
# There is no official solution of this problem
# But, my solution is faster than 90% of python3 online submissions
# It has much memory usage. 메모리는 하위 5% 이지만, 워낙 메모리 적게 먹는 문제라 미세한 차이로 ranking이 갈려서 상관 없음

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        result = ListNode(0)
        result_tail = result
        while l1 != None and l2 != None:
            if l1.val >= l2.val:
                result_tail.next = ListNode(l2.val)
                result_tail = result_tail.next
                l2 = l2.next
                
            else:
                result_tail.next = ListNode(l1.val)
                result_tail = result_tail.next
                l1 = l1.next
        
        
        if l1 == None:
            while l2 != None:
                result_tail.next = ListNode(l2.val)
                result_tail = result_tail.next
                l2 = l2.next
        
        if l2 == None:
            while l1 != None:
                result_tail.next = ListNode(l1.val)
                result_tail = result_tail.next
                l1 = l1.next
        
        return result.next

l1 = ListNode(1)
l1b = ListNode(2)
l1c = ListNode(4)
l1.next = l1b
l1b.next = l1c


l2 = ListNode(1)
l2b = ListNode(3)
l2c = ListNode(4)
l2.next = l2b
l2b.next = l2c
