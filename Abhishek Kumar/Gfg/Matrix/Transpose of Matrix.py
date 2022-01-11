class Solution:
    
    #Function to find transpose of a matrix.
    def transpose(self,matrix, n):
        for i in range(n):
            for j in range(n):
                if i > j:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
