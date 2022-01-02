class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s1=[]
        s1[:0]=s
        n=len(s1)
        for i in range(n):
            if s1[i]==0:
                s1[i]=-1
        l=[0]*n
        sum1=0
        for i in range(n-1):
            sum1+=int(s1[i])
            l[sum1]+=1
        sum2=0
        for i in range(n):
            sum2+=int(l[i])

        return sum2
            
    
            
