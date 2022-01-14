class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split("/")
        stack = []
        for t in tokens:
            if(stack and t==".."):
                stack.pop()
            elif(t not in ["..",'.','']):
                stack.append(t)
        ans = []
        if(len(stack)==0):
            ans.append('/')
        for directory in stack:
            ans.append('/')
            ans.append(directory)
            
        return "".join(ans)