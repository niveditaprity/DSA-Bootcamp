class Solution:
    memo = {}
    def dp(self, n):
            if n <= 1:
                return 1
            if n in self.memo:
                return self.memo[n]
            
            res = 0
            for i in range(n):
                res += self.dp(i) * self.dp(n-i-1)
            
            self.memo[n] = res
            return res
        
    def numTrees(self, n: int) -> int:
        return self.dp(n)