#User function Template for python3


class Solution:
    
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        
        pre = None
        flag = True 
        def dfs(node):
            nonlocal pre, flag
            if not node:
                return 
            dfs(node.left)
            if pre is not None and node.data <= pre.data:
                flag = False
                return 
            pre = node 
            dfs(node.right)
        dfs(root)
        if flag:
            return 1
        return 0
