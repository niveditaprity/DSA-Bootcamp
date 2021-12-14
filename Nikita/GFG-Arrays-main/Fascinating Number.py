#User function Template for python3
class Solution:

	def fascinating(self,n):
	   n1=n*2
	   n2=n*3
	   n3=str(n1)+str(n2)+str(n)
	   lst=list(n3)
	   lst.sort()
	   sum=""
	   for i in lst:
	       sum+=i
       if(sum=="123456789"):
             return True
       else:
            return False
	    
#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input().strip())
        ob = Solution()
        ans = ob.fascinating(n)
        if ans:
            print("Fascinating")
        else: 
            print("Not Fascinating")
        tc -= 1

# } Driver Code Ends
