class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        max_platforms = 1
        needed_platforms = 1
        j = 0
        i = 1
        while(i<n and j<n):
            if(dep[j]<arr[i]):
                j+=1
                max_platforms-=1
            elif(dep[j]>=arr[i]):
                i+=1
                max_platforms+=1
            needed_platforms = max(needed_platforms, max_platforms)
        return needed_platforms