class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        t = digits[-1]+1
        digits[-1] = t%10
        q = t//10
        if(q==0):
            return digits
        n = len(digits)-1
        for i in range(n-1,-1,-1):
            if(q>0):
                t = digits[i]+q
                digits[i] = t%10
                q = t//10
            else:
                break
        if(q>0):
            digits.insert(0,q)
        return digits