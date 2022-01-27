'''
Given a string. Count the number of Camel Case characters in it.

Example 1:

Input:
S = "ckjkUUYII"
Output: 5
Explanation: Camel Case characters present:
U, U, Y, I and I.

â€‹Example 2:

Input: 
S = "abcd"
Output: 0
Explanation: No Camel Case character
present.

Your Task:
You don't need to read input or print anything. Your task is to complete the function countCamelCase() which takes the string S as input and returns the count of the camel case characters in the string.


Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).


Constraints:
1<=|S|<=105

 '''
#User function Template for python3

class Solution:
    def countCamelCase (self,s):
        # your code here
        a=0
        for i in s:
            if i.isupper():
                a+=1
        return a

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    print (ob.countCamelCase (s))

# Contributed By: Pranay Bansal

# } Driver Code Ends
