# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.ptr = -sys.maxsize
        self.stack = []
        self.root = root
        self.curr = root

        

    def next(self):
        c = self.curr
        while c != None:
            self.stack.append(c)
            c = c.left
        res = self.stack.pop()
        self.curr = res.right
        
        return res.val

    def hasNext(self):
        if self.curr != None or len(self.stack)!= 0:
            return True
        
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()