class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
        l=0
        h=len(s)-1
        while l<h:
            if(s[l]!=s[h]):
                withoutl=s[:l]+s[l+1:]
                withouth=s[:h]+s[h+1:]
                if withoutl==withoutl[::-1] or withouth==withouth[::-1]:
                    
                    return True
               
                else:
                    return False
            l+=1
            h-=1
        
