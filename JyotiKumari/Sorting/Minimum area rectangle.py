class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points = sorted(points)
        segs = {}
        max_val = pow(10,10) 
        res = max_val
        
        i = 0
        while i < len(points):
            j = i
            while j < len(points) and points[j][0] == points[i][0]:
                j += 1
            
            for s1 in range(i, j):
                for s2 in range(s1 + 1, j):
                    x = points[s1][0]
                    key = (points[s1][1], points[s2][1])
                    if key in segs:
                        s = (key[1] - key[0]) * (x - segs[key])
                        res = min(s, res)
                    segs[key] = points[s1][0]
            i = j
            
        if res == max_val:
            return 0
        return res