# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')
        
        def dfs(root):
            if(root is None):
                return 0
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            currSum = root.val+left+right

            self.maxSum = max(currSum, self.maxSum)

            return max(root.val+left, root.val+right)
    
        dfs(root)
        return self.maxSum
        
        