class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        
        pq = [[-count, c] for c, count in counter.items()] 
        heapify(pq)
        print(pq)
        t = None
        ret = ''
        
        while pq or t:
            # cannot find solution
            if t and not pq:
                return ''
            
            count, c = heappop(pq)
            
            ret = ret + c
            count = count + 1
            
            if t:
                heappush(pq, t)
                t = None
            
            if count:
                t = [count, c]
                
        return ret