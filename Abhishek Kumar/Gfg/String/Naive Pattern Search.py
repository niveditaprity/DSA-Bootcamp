class Solution:
    
    #Function to check if the given pattern exists in the given string or not.
    def search(self,p,s):
        n = len(s)
        m = len(p)
        for i in range(n - m + 1):
            j=0
            while(j < m):
                if p[j] != s[i+j]:
                    break
                j+=1
            if j==m:
                return True
        return False
                
