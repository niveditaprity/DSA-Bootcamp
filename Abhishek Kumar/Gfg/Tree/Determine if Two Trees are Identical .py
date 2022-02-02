    def isIdentical(self,root1, root2):
        if root1 == None and root2==None:
            return True
        elif root1 == None or root2==None:
            return False
        
        return (root1.data == root2.data) and self.isIdentical(root1.left,root2.left) and self.isIdentical(root1.right,root2.right)
