from collections import OrderedDict

class Solution:
    def firstNonRepeating(self, arr, n): 
        # Complete the function
        answer = 0
        d = OrderedDict()
        for element in arr:
            d[element] = 0
        for element in arr:
            d[element]+= 1
        for key in d:
            if d[key]==1:
                answer = key
                break
        return answer