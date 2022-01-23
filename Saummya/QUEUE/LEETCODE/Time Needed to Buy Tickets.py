class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        s = 0
        for i in range(0, len(tickets)):

            if i < k:
                if tickets[i] > tickets[k]: 
                     s += tickets[k]
                else: 
                    s += tickets[i]
            elif i == k:
                s += tickets[k]

            else:
                if tickets[i] < tickets[k]:
                    s += tickets[i]
                else : 
                    s += tickets[k] - 1
            
        return s
