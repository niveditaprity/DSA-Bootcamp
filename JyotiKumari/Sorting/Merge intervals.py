class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        while(i<len(intervals)-1):
            while(i<len(intervals)-1 and intervals[i][1]>=intervals[i+1][0]):
                if(intervals[i][1]<intervals[i+1][1]):
                    intervals[i][1] = intervals[i+1][1]
                intervals.remove(intervals[i+1])
            i+=1
        return(intervals)