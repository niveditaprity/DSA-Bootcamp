class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n=len(s)
        res=""
        for i in range(0,n):
            for j in range(i,n):
                if all(ch.swapcase() in s[i:j+1] for ch in s[i:j+1]): 
                    if len(s[i:j+1])>len(res):
                        res=s[i:j+1]
        return res
                    
                    
