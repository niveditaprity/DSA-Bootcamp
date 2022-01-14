#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        array.sort()
        j=0
        for i in array:
            if(n==array[-1]):
                j+=1
                if(i==j):
                    pass
                elif(i!=j):
                    return j
                    break
                else:
                    return 
            elif(n!=array[-1]):
                return n

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
