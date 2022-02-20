# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans=0
        if root is None:
            return 0
       
        if root.val <= high and root.val >= low:
            return root.val + self.rangeSumBST(root.right, low, high) +             self.rangeSumBST(root.left, low, high)
        else:
            return self.rangeSumBST(root.right, low, high) + self.rangeSumBST(root.left, low, high)

        
        #iterative approach
        q = deque()
        q.append(root)
        res = 0 
        
        while q: # q = [10]
            node = q.popleft()
            if node.val >= low and node.val <= high:
                res += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return res
