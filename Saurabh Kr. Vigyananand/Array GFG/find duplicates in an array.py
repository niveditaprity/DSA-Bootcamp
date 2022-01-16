class Solution:
    def duplicates(self, arr, n):
        arr.sort()
        
        a=[-1]
        for i in range(0,len(arr)-1):
            if arr[i]==arr[i+1]:
        # print(arr[i])
                a.append(arr[i])
        if(len(a)>1 and a[0]==-1):
            del a[0]
            
        a=set(a)
        a=list(a)
        a.sort()
        
        return a

    


            

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends
