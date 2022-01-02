class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        if(n<3):
            return 0
        l = [0]*3
        i = 0
        while(i<3):
            l[i] = s[i]
            i+=1
        
        if(l[0]!=l[1] and l[1]!=l[2] and l[0]!=l[2]):
                count+=1
        while(i<n):
            l.remove(l[0])
            l.append(s[i])
            if(l[0]!=l[1] and l[1]!=l[2] and l[0]!=l[2]):
                count+=1
            i+=1
    
        return count