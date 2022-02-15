# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        res=[]
        if root:
            stack.append(root)
        
        while(stack):
            top=stack.pop()
            if top:
                res.append(top.val)
                stack.append(top.left)
                stack.append(top.right)
        return res[::-1]