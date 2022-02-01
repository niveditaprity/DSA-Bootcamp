    def rec_InOrder(self,root,lst):
        if root == None:
            return
        self.rec_InOrder(root.left,lst)
        lst.append(root.data)
        self.rec_InOrder(root.right,lst)
        
    def InOrder(self,root):
        lst=[]
        self.rec_InOrder(root,lst)
        return lst
