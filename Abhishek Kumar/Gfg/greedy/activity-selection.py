    def activitySelection(self,n,start,end):
        
        works = []
        
        for i in range(n):
            works.append((start[i],end[i]))
        
        works = sorted(works,key = lambda tup:tup[1])
        
        res = 1
        prev_end = works[0][1]
        
        for i in range(1,n):
            if works[i][0] > prev_end:
                res = res+1
                prev_end = works[i][1]
                
        return res
