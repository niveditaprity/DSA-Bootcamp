#User function Template for python3

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        lst=[]
        m=[]
        A=list(set(A))
        B=list(set(B))
        C=list(set(C))
        lst.extend(A)
        lst.extend(B)
        lst.extend(C)
        lst.sort()
        for i in range(0,len(lst)-2):
            if(lst[i]==lst[i+1]==lst[i+2]):
                m.append(lst[i])
        
        if(len(m)==0):
            return [-1]
        else:
            return m
                
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3


t = int (input ())
for tc in range (t):
    n1, n2, n3 = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    ob = Solution()
    
    res = ob.commonElements (A, B, C, n1, n2, n3)
    
    if len (res) == 0:
        print (-1)
    else:
        for i in range (len (res)):
            print (res[i], end=" ")
        print ()

# } Driver Code Ends
