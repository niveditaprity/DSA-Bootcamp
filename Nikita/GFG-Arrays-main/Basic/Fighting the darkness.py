

class Solution:
    def maxDays(self, arr, n):
        arr.sort()
        return arr[n-1]
        
        # code here

#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        arr = list(map(int,input().split()))
        ob = Solution()
        print(ob.maxDays(arr,n))
# } Driver Code Ends
