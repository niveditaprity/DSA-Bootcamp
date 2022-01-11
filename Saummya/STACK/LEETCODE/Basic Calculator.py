class Solution:
    def calculate(self, s: str) -> int:
        stack = [] # for transactions.
        num = 0
        op = '+'
        res = []
        
        for i,ch in enumerate(s):                
            if ch.isnumeric():
                num = int(ch) + 10*num # to build the num
            elif ch == '+' or ch == '-':
                num = num if op == '+' else -num # op holds the previous value. use that to determine the sign of num
				
                if stack: # if there are any brackets open
                    stack[-1][1].append(num) # add to latest transaction
                else:
                    res.append(num) # else add to base transaction
                op = ch # this will be operator for next logic
                num = 0
            elif ch == ' ':
                num = num if op == '+' else -num
                if stack:
                    stack[-1][1].append(num)
                else:
                    res.append(num)
                num = 0
            elif ch == '(':
                num = num if op == '+' else -num
                if stack:
                    stack[-1][1].append(num)
                else:
                    res.append(num)
                num = 0
                stack.append([op,[]]) # save the current operator
                op = '+'
            elif ch == ')':
                num = num if op == '+' else -num
                stack[-1][1].append(num)
                prevop, temp = stack.pop()
                temp = sum(temp) if prevop == '+' else -sum(temp)
                if stack:
                    stack[-1][1].append(temp)
                else:
                    res.append(temp)
                num = 0
        
        
        num = num if op == '+' else -num #finally if anything is left
        res.append(num)
        
        return sum(res)
