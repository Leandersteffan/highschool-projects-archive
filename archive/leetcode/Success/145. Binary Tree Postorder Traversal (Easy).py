# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #3
        traversal, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                # pre-order, right first
                traversal.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        # reverse result
        return traversal[::-1]
        
        #2
        '''traversal, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # add to result if visited
                    traversal.append(node.val)
                else:
                    # post-order
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return traversal'''
        
        #1
        '''traversal = self.print_inorder(root, '')
        return traversal[:-1].split('*')
        
    def print_inorder(self, start, traversal):
        if start:
            traversal = self.print_inorder(start.left, traversal)
            traversal = self.print_inorder(start.right, traversal)
            traversal += str(start.val) + '*'
        return traversal'''
