class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n=len(s)
        c=0
        for i in range(n):
            s1=s[i:i+3:1]
            set1=set(s1)
            if len(set1)==3:
                c+=1
        return c
            
