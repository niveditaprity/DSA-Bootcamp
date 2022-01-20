class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        ans = [""] * n
        d = {}
        
        for i in range(n):
            d[score[i]] = i
        
        pos = 1
        for val, idx in sorted(d.items(), reverse=True):
            if pos == 1:
                ans[idx] = "Gold Medal"
            elif pos == 2:
                ans[idx] = "Silver Medal"
            elif pos == 3:
                ans[idx] = "Bronze Medal"
            else:
                ans[idx] = str(pos)
                
            pos += 1
            
        
        return ans