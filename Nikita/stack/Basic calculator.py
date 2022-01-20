class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        stack = []
        sign = 1
        num = 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                j = i
                num = 0
                while j < len(s) and s[j].isdigit():
                    num = num*10 + int(s[j])
                    j += 1
                res += sign * num
                i = j
            elif s[i] == '+':
                sign = 1
                i += 1
            elif s[i] == '-':
                sign = -1
                i += 1
            elif s[i] == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
                i += 1
            elif s[i] == ')':
                sign = stack.pop()
                previousLevelResult = stack.pop()
                res = previousLevelResult + sign * res
                i += 1
            else:
                i += 1
                
                
                
        return res
