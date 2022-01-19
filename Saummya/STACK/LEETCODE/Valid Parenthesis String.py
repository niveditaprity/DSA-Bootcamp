class Solution:
    def checkValidString(self, s: str) -> bool:
        Num = 0
		# all * will be used as left parenthesis
        for c in s:
            if c == '(': 
                Num += 1
            elif c == ')': 
                Num -= 1
            else:
                Num += 1
			# check as pointer goes
            if Num < 0: 
                return False
            
        Num = 0
		# all * will be used as right parenthesis
        for c in s[::-1]:
            if c == ')': 
                Num += 1
            elif c == '(': 
                Num -= 1
            else:
                Num += 1
			# check as pointer goes
            if Num < 0: 
                return False
        return True

