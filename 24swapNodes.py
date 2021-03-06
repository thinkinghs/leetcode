# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 21:02:13 2019

@author: Abraham
"""

# https://leetcode.com/problems/swap-nodes-in-pairs/
# medium

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
               
        nodetail = head
        tempfirst = ListNode(0)
        tempsecond = ListNode(0)
        bridge = ListNode(0)
        
        if head.next:
            headPointer = head.next
        else:
            headPointer = head
        
        # node가 None이거나 next node가 None이면 break
        while nodetail and nodetail.next:
            tempfirst = nodetail
            tempsecond = nodetail.next
            bridge.next = tempsecond

            nodetail = nodetail.next.next
            tempfirst.next = nodetail
            tempsecond.next = tempfirst
            bridge = tempfirst

            print(tempsecond.val)
            print(tempfirst.val)
        
        headPointer.next.next.next.val
        
        return headPointer

 # https://leetcode.com/problems/swap-nodes-in-pairs/discuss/11019/7-8-lines-C%2B%2B-Python-Ruby
class bestSolution:
    def swapPairs(self, head):
        dummy = pre = ListNode(0)
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return dummy.next
    
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
