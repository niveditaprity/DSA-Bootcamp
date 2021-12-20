class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        c=0
        for i in range(len(s)):
            s1=s[i:i+3:1]
            s2=set(s1)
            if len(s2)==3:
                c+=1
        return c
            
  
