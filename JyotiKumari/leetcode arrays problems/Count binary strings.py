class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        i = 1
        prev = 0
        curr = 1
        while(i<len(s)):
            if(s[i-1]!=s[i]):
                count+=min(prev, curr)
                prev = curr
                curr = 1
            else:
                curr+=1
            i+=1
        count+=min(prev, curr)
        return count