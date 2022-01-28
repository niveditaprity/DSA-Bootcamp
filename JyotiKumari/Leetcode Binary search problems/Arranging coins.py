class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 0
        high = n
        
        while(low<=high):
            mid = (low+high)//2
            k = mid*(mid+1)//2
            if(k == n):
                return mid
            elif(k > n):
                high = mid - 1
            else:
                low = mid + 1
        return high