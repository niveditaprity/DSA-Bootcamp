class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        seconds=0
        for i in range(len(tickets)):
            if(i<=k):
                seconds+=min(tickets[k], tickets[i])
            else:
                seconds+=min(tickets[k]-1, tickets[i])
        return seconds