class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        #Your code here
        low = 0
        high = N-1
        res = -1
        while low <= high:
            mid = (low + high)//2
            if A[mid] == X:
                return mid 
            elif X < A[mid]:
                high = mid - 1
            else:
                res = mid
                low = mid + 1
        return res
 
#{ 
#  Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            NX=[int(x) for x in input().strip().split()]
            N=NX[0]
            X=NX[1]

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            print(obj.findFloor(A,N,X))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends