
class Solution:
    def transfigure(self, A, B): 
        # code here 
        n = len(A)-1
        m = len(B)-1
        check=0
        for ch in A:
            check+=ord(ch)
        for ch in B:
            check-=ord(ch)
        if(check!=0):
            return -1
        else:
            count=0
            while(n>=0 and m>=0):
                if(A[n]!=B[m]):
                    n = n-1
                    count = count+1
                else:
                    n = n-1
                    m = m-1
        
        return count