# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)
        
        '''traversal = self.print_inorder(root, '')
        return traversal[:-1].split('*')
        
    def print_inorder(self, start, traversal):
        if start:
            traversal = self.print_inorder(start.left, traversal)
            traversal += str(start.val) + '*'
            traversal = self.print_inorder(start.right, traversal)
        return traversal'''
            
