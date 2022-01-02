# USING 2 POINTER CONCEPT

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s)==1 or len(s)==2:
            return True
        #if already a palindrome
        if s==s[::-1]:
            return True
        
        start=0
        end=len(s)-1
        while(start<end):
            if s[start]!=s[end]:
                withoutstart=s[:start]+s[start+1:]
                withoutend=s[:end]+s[end+1:]
                
                if withoutstart==withoutstart[::-1] or withoutend==withoutend[::-1]:
                    return True
                else:
                    return False
            start+=1
            end-=1
            
