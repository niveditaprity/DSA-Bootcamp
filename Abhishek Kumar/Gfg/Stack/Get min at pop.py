def _push(a,n):
    stack = []
    minimum = a[0]
    stack.append(a[0])
    for i in range(1,n):
        minimum = min(a[i],minimum)
        stack.append(minimum)
    return stack

    # code here


#Function to print minimum value in stack each time while popping.    
def _getMinAtPop(stack):
    while len(stack) > 0:
        print(stack.pop(),end=" ")
