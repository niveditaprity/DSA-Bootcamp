class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        count1 = 0
        count2 = 0
        while(start<end):
            if(s[start]==s[end]):
                start+=1
                end-=1
            else:
                start+=1
                count1+=1
        start = 0
        end = len(s)-1
        while(start<end):
            if(s[start]==s[end]):
                start+=1
                end-=1
            else:
                end-=1
                count2+=1
        if (count1==1 or count2==1):
            return True
        if(count1==0 or count2==0):
            return True
        return False