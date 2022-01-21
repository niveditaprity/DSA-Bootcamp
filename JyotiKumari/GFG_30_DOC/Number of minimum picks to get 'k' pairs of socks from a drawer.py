class Solution:
    def find_min(self, a, n, k):
        #Code Here
        ans = -1
        pairs = 0
        opt = 0
        for i in a:
            pairs += i //2
            if(i%2==1):
                opt+=(i-1)//2
            else:
                opt+=(i-2)//2
        if (k > pairs):
            return ans
        if(k<=opt):
            ans = 2*(k-1) + n+ 1
        else:
            ans = 2*opt+(k-opt) + n
        return ans