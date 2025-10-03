'mit beachtung der Regeln des Binary search trees'
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root


'Ohne das der Binary search tree regeln folgt'
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''if root.val == p or root.val == q:
            return root.val'''
        print(root)
        self.out = root
        return self.try_tree(root, p.val, q.val)
        
    
    def check(self, root):
        if root.left:
            self.tree.append(self.check(root.left))
        if root.right:
            self.tree.append(self.check(root.right))
        return root.val
    
    def is_check_True(self, root, p, q):
        print(root)
        self.tree = [root.val]
        self.check(root)
        if p in self.tree and q in self.tree:
            return True
        else:
            return False
        
    def try_tree(self, root, p, q):
        if root.left:
            if self.is_check_True(root.left, p, q):
                self.out = root.left
                self.try_tree(root.left, p, q)
        if root.right:
            if self.is_check_True(root.right, p, q):
                self.out = root.right
                self.try_tree(root.right, p, q)
        return self.out
