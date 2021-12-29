class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles=sorted(piles)[::-1]
        n=len(piles)
        i=1
        j=n-1
        a=0
        while(i<j):
            a+=piles[i]
            i+=2
            j=j-1
        return a
            
