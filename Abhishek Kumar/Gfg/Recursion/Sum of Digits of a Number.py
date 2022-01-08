class Solution:
    def sumOfDigits(self, n):
        '''
        :param n: given number
        :return: sum of digits of n.
        '''
        if n==0:
            return 0
        return n%10 + self.sumOfDigits(n//10)
