class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        start = 0
        end = 1
        count = 1
        while(end<len(prices)):
            if(prices[end-1]-prices[end]==1):
                count+=end-start+1
            else:
                start = end
                count+=end-start+1
            end+=1
        return count