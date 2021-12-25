class Solution:
    def ispalindrome(self, string):
        i = 0
        j = len(string)-1
        while(i<j):
            if(string[i]!=string[j]):
                return False
            i+=1
            j-=1
        return True
        
    def firstPalindrome(self, words: List[str]) -> str:
        for string in words:
            if(self.ispalindrome(string)):
                return string
        return ""