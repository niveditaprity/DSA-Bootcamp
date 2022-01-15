class Solution:
    def reverseWords(self, s):
        # code here
        s+='.'
        stack=[]
        ans=''
        for i in s:
            if i=='.':
                while stack:
                    ans+=stack.pop()
                ans+='.'
            else:
                stack.append(i)
        
        return ans[:-1]