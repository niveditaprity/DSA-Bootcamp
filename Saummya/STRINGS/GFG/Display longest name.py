'''
Given a list of names, display the longest name.


Example:

Input:
N = 5
names[] = { "Geek", "Geeks", "Geeksfor",
  "GeeksforGeek", "GeeksforGeeks" }

Output:
GeeksforGeeks
 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function longest() which takes the array names[] and its size N as inputs and returns the Longest name in the list of names.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

 

Constraints:
1 <= N <= 100
1 <= |length of name| <= 1000
'''
#User function Template for python3

class Solution:
    def longest(self, names, n):
    	# code here
    	max1=0
    	for ele in names:
    	    k=len(ele)
    	    if max1<k:
    	        maxStr= str(ele)
    	        max1=k
    	return maxStr
    	
    	

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
    	n=int(input())
    	names = []
    	for i in range(n):
    		names.append(input())
    	ob = Solution()
    	print(ob.longest(names, n))
    	
    	T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
