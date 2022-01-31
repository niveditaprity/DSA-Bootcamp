'''
You are given an array arr of size N. You need to push the elements of the array into a stack and then print them while popping.

Example 1:

Input:
n = 5
arr = {1 2 3 4 5}
Output:
5 4 3 2 1
Example 2: 

Input: 
n = 7
arr = {1 6 43 1 2 0 5}
Output: 
5 0 2 1 43 6 1
 

Your Task:
Since this is a function problem, you don't need to take any input. Just complete the provided functions _push() and _pop().

Constraints:
1 <= Ai <= 10^7
'''
#User function Template for python3
from collections import deque
#_push function to insert elements of array to stack
def _push(arr):
    #return a stack with all elements of arr inserted in it
    stack=deque()
    for i in arr:
        stack.append(i)
    return stack
    

#_pop function to print elements of the stack remove as well
def _pop(stack):
    #print top and pop for each element until it becomes empty
    while stack:
        print(stack.pop(),end=" ")
    print()
   
        



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr=[int(i) for i in input().split()]
        stack = _push(arr)
        _pop(stack)

# } Driver Code Ends
