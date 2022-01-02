from collections import OrderedDict

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr, n):
        
        #arr : given array
        #n : size of the array
        d = OrderedDict()
        for element in arr:
            d[element] = 0
        for element in arr:
            d[element]+=1
        index = 1
        for element in d:
            if(d[element]>1):
                return index
            index+=1
        return -1