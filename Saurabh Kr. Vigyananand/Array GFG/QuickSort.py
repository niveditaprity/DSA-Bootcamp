#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.

    def partition(self,arr,low,high):
        
        start=low
        pivot=arr[low]
        end=high
        while(start<end):
            while(start<len(arr) and arr[start]<=pivot):
                start+=1
                #print(start)
            while(arr[end]>pivot):
                end-=1
                #print(end)
            if(start<end):
                arr[start],arr[end]=arr[end],arr[start]
                
              #print(start,end)
    
        arr[low],arr[end]=arr[end],arr[low]
        return end# code here

    def quickSort(self,arr,low,high):
        
        if(low<high):
            loc = self.partition(arr,low,high)
            self.quickSort(arr,low,loc-1)
            self.quickSort(arr,loc+1,high)
        
  
 
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends
