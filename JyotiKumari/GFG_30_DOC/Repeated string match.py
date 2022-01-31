
class Solution:
    def repeatedStringMatch(self, A, B):
        # code here
        n = len(A)
        m = len(B)
       
        if(m < n):
            if B in A:
                return 1
            elif (B*2) in A:
                return 2
       
        count1 = int(m/n)
        count2 = int(m/n) + 1
        count3 = int(m/n) + 2
       
        if( B in (A*count1) ):
            return count1
        elif( B in (A*count2) ):
            return count2
        elif( B in (A*count3) ):
            return count3
        else:
            return -1