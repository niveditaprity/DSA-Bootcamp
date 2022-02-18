# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        def bfs(node, level):
            if len(levels) == level:
                levels.append(deque([node.val]))
            else:
                if level % 2 == 0:
                    levels[level].append(node.val)
                else:
                    levels[level].appendleft(node.val)
            if node.left:
                bfs(node.left, level+1)
            if node.right:
                bfs(node.right, level+1)
        bfs(root, 0)
        return levels
    
    #iterative
    '''
        # iterative
    def zigZaglevelOrderTraversal(root):
        
        if not root:
            return levels

        level = 0
        q = deque([root])
        levels = []
        while q:
            levels.append(deque([]))

            for i in range(len(q)):
                node = q.popleft()
                if level % 2 == 0:
                    levels[level].append(node.val)
                else:
                    levels[level].appendleft(node.val)
                if node.left:
                    q.append(node.left)  
                if node.right:
                    q.append(node.right)
            level += 1
        return levels'''
