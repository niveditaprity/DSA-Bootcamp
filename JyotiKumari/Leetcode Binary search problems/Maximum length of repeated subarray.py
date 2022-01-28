class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        l = [[0 for i in range(m+1)] for j in range(n+1)]
        ans = 0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if(nums1[i-1]==nums2[j-1]):
                    l[i][j] = l[i-1][j-1]+1
                else:
                    l[i][j]=0
                ans = max(ans, l[i][j])
                
        return ans