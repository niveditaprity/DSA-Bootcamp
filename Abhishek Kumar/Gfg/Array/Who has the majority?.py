    def majorityWins(self, arr, n, x, y):
        d = dict()
        for elem in arr:
            if elem in d:
                d[elem] += 1
            else:
                d[elem] = 1
        
        if x in arr:
            c_x = d[x]
        else:
            c_x = 0
            
        if y in arr:
            c_y = d[y]
        else:
            c_y = 0
            
        if c_x == c_y :
            if x < y :
                return x
            else:
                return y
                
        elif c_x < c_y:
            return y
        else:
            return x
            
