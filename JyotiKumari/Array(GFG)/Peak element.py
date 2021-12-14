class Solution:   
    def peakElement(self,arr, n):
        # Code here
        if(n==1 or (arr[0]>=arr[1])):
            return 0
        if(n==2 and arr[1]>=arr[0]):
            return 1
        if(arr[-1]>=arr[-2]):
            return n-1   
        for i in range(1,n-1):
            if(arr[i]>=arr[i-1] and arr[i]>=arr[i+1]):
                return i
        
        return -1