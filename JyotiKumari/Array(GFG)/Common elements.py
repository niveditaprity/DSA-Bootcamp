class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        d = {}
        l = []
        for element in B:
            d[element]=0
        for element in C:
            d[element]=0
        for element in A:
            d[element] =  "i"
        for element in B:
            if(d[element]=="i"):
                d[element]+="j"
        for element in C:
            if(d[element]=="ij"):
                d[element]+="k"
                l.append(element)
        if(len(l)==0):
            l.append(-1)
        return l