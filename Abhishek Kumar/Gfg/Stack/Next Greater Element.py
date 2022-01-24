class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        res = []
        s = []
        n = len(arr)
        
        s.append(arr[n-1])
        res.append(-1)
        
        for i in range(n-2,-1,-1):
            if s[-1] > arr[i]:
                res.append(s[-1])
                s.append(arr[i])
            else:
                while len(s) > 0 and s[-1] < arr[i]:
                    s.pop()
                if len(s) == 0:
                    res.append(-1)
                else:
                    res.append(s[-1])
                s.append(arr[i])
        res = res[::-1]
        return res
