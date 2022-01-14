class Solution:
 
    #Function to add two matrices.
    def sumMatrix(self,A,B):
        # code here
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            return []
            
        res = []
        for i in range(len(A)):
            temp = []
            for j in range(len(A[0])):
                temp.append(A[i][j] + B[i][j])
            res.append(temp)
            
        return res
