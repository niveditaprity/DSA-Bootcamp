# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) ->List[int]:
        return self.right(root,[],level = 0)

    def right(self,root,array,level):
        if root == None:
            return
        level += 1   
        if level > len(array):
            array.append(root.val)
        self.right(root.right,array,level)
        self.right(root.left,array,level)
        level -= 1 
        
        return array
 

    