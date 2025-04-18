# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        res = []
        if not root:
            return res
        while q:
            L = len(q)
            for i in range(L):
                curr = q.popleft()
                if i == L - 1:
                    res.append(curr.val)
                l = curr.left
                r = curr.right
                if l:
                    q.append(l)
                if r:
                    q.append(r)
        return res