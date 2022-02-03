    def isSumProperty(self, root):
        # code here
        if root == None:
            return 1
        if root.left == None and root.right ==  None:
            return 1
            
        summ = 0
        if root.left != None:
            summ+=root.left.data
        if root.right != None:
            summ += root.right.data
            
        if(summ == root.data) and self.isSumProperty(root.left) and self.isSumProperty(root.right):
            return 1
        else:
            return 0
