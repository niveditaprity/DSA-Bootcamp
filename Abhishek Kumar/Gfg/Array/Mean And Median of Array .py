    def median(self,A,N):
        A.sort()
        if N%2 == 0:
            return (A[N//2]+A[N//2-1])//2 
        else :
            return A[N//2]
            
    #Function to find mean of the array elements.   
    def mean(self,A,N):
        ##Your code here
        return sum(A)//N
