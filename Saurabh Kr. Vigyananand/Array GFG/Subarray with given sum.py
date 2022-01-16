#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s):
        # Initialize curr_sum as
        # value of first element
        # and starting point as 0 
        A = []
        curr_sum = arr[0]
        j = 0

        # Add elements one by 
        # one to curr_sum and 
        # if the curr_sum exceeds 
        # the sum, then remove 
        # starting element 
        i = 1
        while i <= n:
        
            # If curr_sum exceeds
            # the sum, then remove
            # the starting elements
            while curr_sum > s and j < i-1:
        
                curr_sum = curr_sum - arr[j]
                j += 1
            
            # If curr_sum becomes
            # equal to sum, then
            # return true
            if curr_sum == s:
                A.append(j+1)
                A.append(i)
                return A

            # Add this element 
            # to curr_sum
            if i < n:
                curr_sum = curr_sum + arr[i]
            i += 1

        # If we reach here, 
        # then no subarray
        A.append(-1)
        return A
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
