class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        
        #code here
        arr = []
        for i in range(n):
            arr.append(a[i])
        for i in range(m):
            arr.append(b[i])
        
        return len(set(arr))