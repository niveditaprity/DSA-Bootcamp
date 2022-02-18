# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        lheight=self.height(root.left)
        rheight=self.height(root.right)
        
        ldia=self.diameterOfBinaryTree(root.left)
        rdia=self.diameterOfBinaryTree(root.right)
        
        return max(lheight+rheight,max(ldia,rdia))
    
    def height(self,root):
        if root is None:
            return 0
        else:
            return 1+ max(self.height(root.left),self.height(root.right))
