    def rotateArr(self,A,D,N):
        temp = []
        for i in range(D):
            temp.append(A[i])
            
        for i in range(D,N):
            A[i-D] = A[i]
        
        ind = N-D
        for i in range(D):
            A[ind] = temp[i]
            ind += 1
            
