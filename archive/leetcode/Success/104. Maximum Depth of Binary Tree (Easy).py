# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        n, x = 0, 0
        if root.left:
            n = self.maxDepth(root.left)
        if root.right:
            x = self.maxDepth(root.right)
        if n > x:
            return n + 1
        else:
            return x + 1
