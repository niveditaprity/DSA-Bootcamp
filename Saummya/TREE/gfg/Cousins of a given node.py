'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def printCousins(self, root, node_to_find):
        #code here
        if root==node_to_find:
            return [-1]
        ans=[]
        f=False
        ans.append(root)
        while(len(ans)!=0 and not f):
            s=len(ans)
            while(s!=0):
                p=ans.pop(0)
                if p.left==node_to_find or p.right==node_to_find:
                    f=True
                else:
                    if p.left:
                        ans.append(p.left)
                    if p.right:
                        ans.append(p.right)
                s-=1
        if f:
            if len(ans)==0:return [-1]
            else:
                res=[]
                for i in ans:
                    res.append(i.data)
                return res
        else:
            return [-1]
