def matching(a,b):
    if a == '(' and b== ')' or a=='{' and b=='}' or a =='[' and b==']':
        return True
    else:
        return False
        
def isBalanced(arr):
    s = []
    n = len(arr)
    for i in range(n):
        if arr[i] in ['(','{','[']:
            s.append(arr[i])
        else:
            e = arr[i]
            if len(s) == 0 :
                return "NO"
            top = s.pop()
            if matching(top,e) == False:
                return "NO"
    if len(s) == 0:
        return "YES"
    else:
        return "NO"
