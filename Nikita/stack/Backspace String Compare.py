class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
         def bsString(string):
            res = []
            for c in string:
                if c != '#':
                    res.append(c)
                else:
                    res = res[:-1]
            return res
         return bsString(s)==bsString(t)
