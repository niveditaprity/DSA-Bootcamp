class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c]+=1
        for i in range(len(s)):
            if(freq[s[i]]==1):
                return i
        return -1