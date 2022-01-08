class Solution:
    def RecursivePower(self,n,p):
        '''
        return value of n^p recursively;
        '''
        # code here
        if p == 0:
            return 1
        return n*self.RecursivePower(n,p-1)
