#User function Template for python3

class Solution:
    # return true/false denoting whether the tree is Symmetric or not
    def isSymmetric(self, root):
        # Your Code Here
         return self.symmetic(root,root)
        
    def symmetic(self,root1,root2):
        if not root1 and not root2:
            return True
        if root1 is not None and root2 is not None:
            if root1.data==root2.data:
                 return (self.symmetic(root1.left,root2.right) and self.symmetic(root1.right,root2.left))
        return False
