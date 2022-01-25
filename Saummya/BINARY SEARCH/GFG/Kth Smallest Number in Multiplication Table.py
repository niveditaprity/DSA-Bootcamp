'''
Given three integers M, N and K. Consider a grid of M * N, where mat[i][j] = i * j (1 based index). The task is to return the Kth smallest element in the M * N multiplication table.
 

Example 1:

Input:
M = 3, N = 3
K = 5
Output: 3
Explanation: 

The 5th smallest element is 3. 


Example 2:

Input:
M = 2, N = 3
K = 6
Output: 6 
'''
#SOLUTION
#APPROACH1:
class Solution(object):
    def findKthNumber(self, m, n, k):
        #Write your code here
        l=[]
        for i in range(1,m+1):
            for j in range(1,n+1):
                l.append(i*j)
        l.sort()
        return l[k-1]
'''
FOR THIS APPROACH:
Test Cases Passed: 
210 /  261
'''
#-----------------------------------------------------------------
#ALL TEST CASES PASSESE USING BINARY SEARCH APPROCH
class Solution(object):
    def findKthNumber(self, m, n, k):
        #Write your code here
        lo,hi = 0,m*n+1
        while lo<hi:
            mid = (lo+hi)//2
            val = 0
            for i in range(m):
                val+=min(n,(mid//(i+1)))
            if val>=k:
                hi = mid
            else:
                lo = mid+1
        return hi
        
        
        '''
        l=[]
        for i in range(1,m+1):
            for j in range(1,n+1):
                l.append(i*j)
        l.sort()
        return l[k-1]
        '''

#{ 
#  Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    arr = list(map(int, input().split())) 
    ob = Solution()
    print(ob.findKthNumber(arr[0],arr[1], arr[2]))
# } Driver Code Ends
