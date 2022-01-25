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

        #APPROACH-2
        class Solution:
            def firstUniqChar(self, s: str) -> int:
                n=len(s)
                i=0
                while(n>i):
                    count=0
                    for j in range(n):
                        if s[i]==s[j]:
                            count+=1
                    i+=1
                    if count==1:
                        return i-1

                return -1
