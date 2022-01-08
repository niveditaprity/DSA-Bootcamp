class Solution:
    #Complete this function
    def power(self,N,R):
        #Your code here
        if R == 0:
            return 1
        ans = self.power(N,R//2)
        if R & 1:
            return (N * ans*ans)%(10**9+7)
        else:
            return (ans * ans)%(10**9+7)
