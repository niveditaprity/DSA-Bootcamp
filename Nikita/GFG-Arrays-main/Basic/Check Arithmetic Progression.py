#User function Template for python3


class Solution:
    
    def checkIsAP(self, arr, n):
        
        arr.sort()
        c=arr[1]-arr[0]
        for i in range(n-1):
            if arr[i+1]-arr[i]!=c:
                return 0
            
            
        return 1
                
                
            
        
        # code here
        
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3


#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    # l=list(map(int,input().split()))
    # n=l[0]
    # x=l[1]
    # y=l[2]
    a = list(map(int,input().split()))
    ob = Solution()
    ans=ob.checkIsAP(a,n)
    if(ans==True):
        print("YES")
    else:
        print("NO")
# } Driver Code Ends
