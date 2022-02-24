# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        return self.checkNodes(root.left, root.right)
       
    def checkNodes(self,left,right):
        if left==None and right==None:
            result= True
        elif left is None and right is not None:
            result= False
        elif left is not None and right is None:
            result= False
        else:
            if left.val!=right.val:
                result= False
            else:
                result=self.checkNodes(left.left, right.right)
                if result:
                    result = self.checkNodes(left.right, right.left)
        return result
        
