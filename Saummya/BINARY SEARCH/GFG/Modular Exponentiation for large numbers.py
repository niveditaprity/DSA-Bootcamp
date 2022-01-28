'''
Implement pow(x, n) % M.
In other words, given x, n and M, find (xn) % M.
 

Example 1:

Input:
x = 3, n = 2, m = 4
Output:
1
Explanation:
32 = 9. 9 % 4 = 1.
Example 2:

Input:
x = 2, n = 6, m = 10
Output:
4
Explanation:
26 = 64. 64 % 10 = 4.

Your Task:
You don't need to read or print anything. Your task is to complete the function PowMod() which takes integers x, n and M as input parameters and returns xn % M.
 

Expected Time Complexity: O(log(n))
Expected Space Complexity: O(1)
 

Constraints:
1 ≤ x, n, M ≤ 109
'''
#SOLUTION:
#1----------------------
class Solution:
	def PowMod(self, x, n, m):
		# Code here
		k=x**n
		l=k%m
		return l
		
    #-------------------------
    #2------------------------
    class Solution:
        def PowMod(self, x, n, m):
          # Code here
          return pow(x,n)%m
        
#3----------------------------------------------------------
#-------------------------------------------------------------
    #User function Template for python3

class Solution:
	def PowMod(self, x, n, m):
		# Code here
		#concept:-- >  (ab) mod p = ( (a mod p) (b mod p) ) mod p 
		res = 1
		x = x % m
		if (x == 0):
            return 0
            
        while (n > 0) :
         
        # If y is odd, multiply
        # x with result
            if ((n & 1) == 1) :
                res = (res * x) % m
     
            # y must be even now
            n = n >> 1      # y = y/2
            x = (x * x) % m
         
        return res
		
		


		

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		x, n , m = input().split()
		x = int(x)
		n = int(n) 
		m = int(m)
		ob = Solution();
		ans = ob.PowMod(x, n, m)
		print(ans)
# } Driver Code Ends
