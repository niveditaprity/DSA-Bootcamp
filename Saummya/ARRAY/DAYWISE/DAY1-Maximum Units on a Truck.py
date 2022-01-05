class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sortedBox = []
        ans = 0
        
        for count, units in boxTypes:
            sortedBox.append((units, count))
        
        sortedBox.sort()
        
        while sortedBox and truckSize>0:
            units, count = sortedBox.pop()
            d = min(count, truckSize)
            truckSize -= d
            ans += d*units
            
        return ans
