# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        hashmap = {}
        res = set()
        res.add(root)
        parent = TreeNode(-1)
        parent.left = root
        self.dfs(root, parent, hashmap, "left")
        for deleteItem in to_delete:
            cur = hashmap[deleteItem][0]
            if cur in res:
                res.remove(cur)
            else:
                p = hashmap[deleteItem][1]
                if hashmap[deleteItem][2] == "left":
                    p.left = None
                else:
                    p.right = None
            if cur.left:
                res.add(cur.left)
            if cur.right:
                res.add(cur.right)
            del cur
        return list(res)
        
        
    def dfs(self, node, parent, hashmap, direction):
        if not node: return
        hashmap[node.val] = (node, parent, direction)
        self.dfs(node.left, node, hashmap, "left")
        self.dfs(node.right, node, hashmap, "right")