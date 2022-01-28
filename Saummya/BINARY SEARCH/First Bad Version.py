# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        for i in range(n):
            if isBadVersion(i):
                return i
            
        return n          
        '''
        
        start=0
        end=n-1
        
        while start<=end:
            mid=(start+end)//2
            if not isBadVersion(mid):
                start=mid+1
            else:
                end=mid-1
                
        return start
