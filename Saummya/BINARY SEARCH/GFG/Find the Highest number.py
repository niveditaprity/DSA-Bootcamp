'''
QUESTION:
Given an array in such a way that the elements stored in array are in increasing order initially and then after reaching to a peak element , elements stored are in decreasing order. Find the highest element.
Note: A[i] != A[i+1]
 

Example 1:

Input:
11
1 2 3 4 5 6 5 4 3 2 1
Output: 6
Explanation: Highest element is 6.
Example 2:

Input:
5
1 2 3 4 5
Output: 5
Explanation: Highest element is 5.

 

Your Task:
You don't need to read or print anything. Your task is to complete the function findPeakElement() which takes the array as the input parameter and returns teh highest element.
 

Expected Time Complexity: O(log(n))
Expected Space Complexity: O(1)
 

Constraints:
2 <= Size of array <= 200
1 <= Elements of the array <= 100000 
'''
#SOLUTION:
#User function Template for python3

class Solution:
	def findPeakElement(self, a):
		# Code here
		k=max(a)
		return k


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		a = list(map(int,input().split()))
		ob = Solution();
		ans = ob.findPeakElement(a)
		print(ans)




# } Driver Code Ends
