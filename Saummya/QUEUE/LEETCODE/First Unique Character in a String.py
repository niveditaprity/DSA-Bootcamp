class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique_chars = {}
        repeated = set()
        for i, c in enumerate(s):
            if c in repeated: continue
            if c in unique_chars: 
                del unique_chars[c]
                repeated.add(c)
            else :
                unique_chars[c] = i
        
        if(len(unique_chars) > 0):
            return min(unique_chars.values())
        else :
            return -1
