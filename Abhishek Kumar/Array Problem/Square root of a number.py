class Solution:
    def floorSqrt(self, x): 
        res = -1
        low = 1
        high = x
        
        while low <= high :
            mid = (low + high)//2
            sq_mid = mid * mid
            if sq_mid == x:
                return mid
            elif sq_mid > x:
                high = mid - 1
            else:
                low = mid + 1
                res = mid
        return res
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            x=int(input())
            
            print(Solution().floorSqrt(x))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends