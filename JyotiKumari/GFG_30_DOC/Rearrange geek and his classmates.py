
class Solution:
    def prank(self, a, n): 
        #code here
        l = n*[0]
        for i in range(n):
            l[i] = a[a[i]]
        for i in range(n):
            a[i] = l[i]
