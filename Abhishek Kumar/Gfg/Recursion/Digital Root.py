class Solution:
    def digitalRoot(self, n):
        '''
        :param n: given number 
        :return: digital root as defined
        '''
        if n < 10:
            return n
        s = 0
        while(n>0):
            s = s+n%10
            n=n//10
            
        return self.digitalRoot(s)
