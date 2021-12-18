
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        water = 0
        lmax = [0]*n
        rmax = [0]*n
        lmax[0] = arr[0]
        rmax[n-1] = arr[n-1]
        for i in range(1,n):
            lmax[i] = max(arr[i],lmax[i-1])
        for i in range(n-2,-1,-1):
            rmax[i] = max(arr[i],rmax[i+1])
        for i in range(n):
            water = water + min(lmax[i],rmax[i]) -  arr[i]
        return water
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code