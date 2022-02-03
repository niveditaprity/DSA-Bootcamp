    def levelOrder(self,root):
        # Code her
        if root == None:
            return []
        lst = []
        q = []
        q.append(root)
        while len(q) > 0:
            curr = q.pop(0)
            lst.append(curr.data)
            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)
        return lst
