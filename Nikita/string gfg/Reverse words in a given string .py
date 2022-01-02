 def reverseWords(self,S):
        s1=""
        s=list(S.split("."))
        for i in range(len(s)):
            if i==0:
                s1+=s.pop()
            else:
                s1=s1+"."+s.pop()
        return s1
