'''
Given a string consisting of lowercase english alphabets, reverse only the vowels present in it and print the resulting string.

Example 1:

Input:
S = "geeksforgeeks"
Output: geeksforgeeks
Explanation: The vowels are: e, e, o, e, e
Reverse of these is also e, e, o, e, e.
â€‹
Example 2:

Input: 
S = "practice"
Output: prectica
Explanation: The vowels are a, e
Reverse of these is e, a.

Your Task:
You don't need to read input or print anything. Your task is to complete the function modify() which takes the string S as input and returns the resultant string by reversing only the vowels present in S.


Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(|S|).


Constraints:
1<=|S|<=105

 '''
#User function Template for python3

class Solution:
    def modify(self, s):
        l=[]
        for i in range(len(s)):
            if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
                l.append(s[i])
        l = l[::-1]
        k=0
        res = ""
        for i in range(len(s)):
            if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
                res+=l[k]
                k+=1
            else:
                res+=s[i]
        return res
        
    
        
        
        '''
        
            # code here
            n=len(s)
            s1=""
            #vow=['a','e','i','o','u']
            i=0
            #j=n-1
            while(i<n):
                if s[i]in ['a','e','i','o','u']:
                    s1+=s[i]
                    i+=1
            #k=s1[::-1]
            return s1[::-1]
        '''
          
            
 
                
                
                
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.modify(s)
        print(ans)
# } Driver Code Ends
