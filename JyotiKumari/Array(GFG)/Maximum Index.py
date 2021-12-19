
class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self,A, N): 
        ##Your code here
        left = [0]*N
        left[0] = A[0]
        for i in range(1,N):
            left[i] = min(A[i], left[i-1])
        right = [0]*N
        right[-1] = A[N-1]
        for i in range(N-2,-1,-1):
            right[i] = max(A[i], right[i+1])
        x = 0
        y = 0
        ans = -1
        while(x<N and y<N):
            if(right[y]>=left[x]):
                ans = max(ans, y-x)
                y+=1
            else:
                x+=1
        return ans