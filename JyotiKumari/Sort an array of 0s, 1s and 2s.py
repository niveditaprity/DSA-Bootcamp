class Solution:
    def sort012(self,arr,n):
        # code here
        i=0
        c0 = arr.count(0)
        c1 = arr.count(1)
        c2 = arr.count(2)
        while(c0):
            arr[i]=0
            i+=1
            c0-=1
        
        while(c1):
            arr[i]=1
            i+=1
            c1-=1
           
        while(c2):
            arr[i]=2
            i+=1
            c2-=1