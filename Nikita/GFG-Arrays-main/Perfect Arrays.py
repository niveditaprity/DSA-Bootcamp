#User function Template for python3

class Solution:
    def IsPerfect(self,arr,n):
        #Complete the function
        a=reversed(arr)
        if a==arr:
            return a
            
        
       
            


#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    if(ob.IsPerfect(arr,n)):
        print("PERFECT")
    else:
        print("NOT PERFECT")
    
# } Driver Code Ends
