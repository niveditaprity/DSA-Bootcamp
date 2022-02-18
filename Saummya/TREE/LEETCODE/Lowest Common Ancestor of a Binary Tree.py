# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.LCA = None
        def recur(root):
            if not root:
                return False
            me = (root.val==p.val or root.val==q.val)
            left = recur(root.left)
            right = recur(root.right)
            if (left and right) or (me and right) or (me and left):
                self.LCA = root
            return left or right or me
        recur(root)
        return self.LCA
        
        
        '''
        if root.val==p.val or root.val==q.val:
            return root
        if not root.left and not root.right:
            return None
        
        if root.left:
            left=lowestCommonAncestor(root.left,p,q)
        if root.right:
            right=lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        if left==None:
            return right
        else:
            return left'''
