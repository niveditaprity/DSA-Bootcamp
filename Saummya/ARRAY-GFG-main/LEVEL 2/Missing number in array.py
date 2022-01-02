#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        # code here
        sum1=0
        totalSum=n*(n+1)//2
        for i in range(n-1):
            sum1=sum1+array[i]
        
        return totalSum-sum1
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends
