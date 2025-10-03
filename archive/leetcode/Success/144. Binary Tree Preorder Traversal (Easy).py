# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret
        
        #2
        '''traversal = self.print_inorder(root, '')
        return traversal[:-1].split('*')
        
    def print_inorder(self, start, traversal):
        if start:
            traversal += str(start.val) + '*'
            traversal = self.print_inorder(start.left, traversal)
            traversal = self.print_inorder(start.right, traversal)
        return traversal'''
