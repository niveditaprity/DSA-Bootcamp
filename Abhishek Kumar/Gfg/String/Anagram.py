class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        n1=len(a)
        n2=len(b)
        if n1 != n2 :
            return False
        char=[0]*123         # Ascii value of small a to small z is till 122  
        for i in range(n1):
            char[ord(a[i])]+=1
            char[ord(b[i])]-=1
        for i in range(n1):
            if char[ord(a[i])] != 0 :
                return False
        return True
