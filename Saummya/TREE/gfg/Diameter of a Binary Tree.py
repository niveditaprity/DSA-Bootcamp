#User function Template for python3



class Solution:
    
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        # Code here
        self.height(root)
        return self.res
        
        
        '''
        if root is None:
            return 0
        lh=self.height(root.left)
        rh=self.height(root.right)
        
        ldia=self.diameter(root.left)
        rdia=self.diameter(root.right)
        
        return max(lh+rh,max(ldia,rdia))'''
        
        
    
    res=0
    def height(self,root):
        if root is None:
            return 0
        lh=self.height(root.left)
        rh=self.height(root.right)
        
        self.res=max(self.res,lh+rh+1)
        
        return max(lh,rh)+1
