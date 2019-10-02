# https://leetcode.com/problems/same-tree/
# easy
# Good problem to understand Tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # p and q are both None
        # Tree search 하면서 leaf까지 도달할 때까지 value들이 같았다면 아래 if에 의해 최종적으로 True가 됨
        # leaf의 left와 right는 None이니 자연스럽게 True return하기 때문에.
        if not p and not q:
            return True
        # one of p and q is None
        # 위에서 둘 다 None인 경우는 return True 했으니, 둘 다 None인 경우 이 로직에 올 수 없음.
        # if or 이용하면 둘 중 한 개만 None인 경우 False를 return
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        # recursive는 위와 같이 종료 조건을 적어준 뒤에 아래처럼 recursive 호출
        # recursive 거치면서 아래 condition logic이 많아질 것이고, 하위의 condition 중에 False가 한개라도 있으면 바로 False return. 다 True이면 True return
        # recursive이기에 모든 분화된 하위 과정을 다 거친 후에 가장 처음의 condition이 return 된다.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


''' Approach2 using iteration
from collections import deque
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True
        
        deq = deque([(p,q)])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        
        return True
'''
