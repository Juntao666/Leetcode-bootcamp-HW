class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def __init__(self):
            self.res = None

        def dfs(node):
            if node == None:
                return False
            mid = ((node.val == p.val) or (node.val == q.val))
            left = dfs(node.left)
            right = dfs(node.right)
            if mid + left + right == 2:
                self.res = node
            return mid or left or right
        dfs(root)
        return self.res