class Solution:
    
    #Function to return sum of upper and lower triangles of a matrix.
    def sumTriangles(self,matrix, n):
        # code here 
        lower = 0
        upper = 0
        for i in range(n):
            for j in range(n):
                if i <= j:
                    upper += matrix[i][j]
                if i >= j:
                    lower += matrix[i][j]
        return [upper,lower]
                    
