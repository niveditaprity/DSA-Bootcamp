class Solution:
    def josephus(self,n,k):
        #Your code here
        def My_josephus(n,k):
            if n==0:
                return 0
            return (My_josephus(n-1,k)+k)%n
            
        return My_josephus(n,k) + 1
