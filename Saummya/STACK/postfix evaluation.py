        def eval_postfix(arr):
            stack=[]
            operator=['+','-','*','/','%','^']
            for item in arr:
                if item not in operator:
                    stack.append(item)
                else:
                    first=int(stack.pop())
                    sec= int(stack.pop())
                    
                    if item=="+":
                        stack.append(sec+first)
                        
                    if item=="-":
                        stack.append(sec-first)
                        
                    if item=="*":
                        stack.append(sec*first)
                    
                    if item=="/":
                        stack.append(sec/first)
                        
                    if item=="%":
                        stack.append(sec%first)
                        
            return stack[-1]
        
