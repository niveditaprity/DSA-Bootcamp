class Solution:
    def checkValidString(self, s: str) -> bool:
        open_parenthesis = []
        star = []
        for i in range(len(s)):
            if(s[i]=='*'):
                star.append(i)
            elif(s[i]=='('):
                open_parenthesis.append(i)
            else:
                if(open_parenthesis):
                    open_parenthesis.pop()
                elif(star):
                    star.pop()
                else:
                    return False
        while(open_parenthesis):
            if not star:
                return False
            elif(open_parenthesis[-1]<star[-1]):
                star.pop()
                open_parenthesis.pop()
            else:
                return False
            
        return True