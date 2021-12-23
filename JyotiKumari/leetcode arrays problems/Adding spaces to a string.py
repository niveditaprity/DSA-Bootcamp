class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        l  = []
        j = spaces[0]
        k = 0
        for i in range(len(s)):
            if(i==j):
                l.append(" ")
                if(k<len(spaces)-1):
                    k+=1
                    j = spaces[k]
            l.append(s[i])
        return "".join(l)