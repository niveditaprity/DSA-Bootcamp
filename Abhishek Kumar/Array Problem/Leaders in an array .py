
class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        Leaders=[]
        Leaders.append(A[N-1])
        cur_max = A[N-1]
        for i in range(N-2,-1,-1):
            if A[i] >= cur_max:
                cur_max = A[i]
                Leaders.append(cur_max)
        Leaders.reverse()
        return Leaders
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends