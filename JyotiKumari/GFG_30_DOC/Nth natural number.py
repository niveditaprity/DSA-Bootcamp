class Solution:
    def findNth(self,N):
        #code here
        result = 0
        t = 1
        while(N>0):
            result = result+t*(N%9)
            t = t*10
            N = N//9
        return result