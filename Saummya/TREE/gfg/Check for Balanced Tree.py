#User function Template for python3


'''class Node: 
    # Constructor to create a new Node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None'''


#Function to check whether a binary tree is balanced or not.
class Solution:
    def isBalanced(self,root):
        ans=[True]
        self.heightcheck(root,ans)
        if ans[0]==False:
            return False
        else:
            return True
            
            
    def heightcheck(self,root,ans):
        if root==None:
            return 0
        lh=self.heightcheck(root.left,ans)
        rh=self.heightcheck(root.right,ans)
        if abs(lh-rh)>1:
            ans[0]=False
        return max(lh,rh)+1 
