class Solution:
    
    #Function to count the number of substrings that start and end with 1.
    def binarySubstring(self,n,s):
        count = 0
        for i in range(n):
            if s[i] == '1':
                count +=1
        return (count*(count-1))//2
