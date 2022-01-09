#Function to locate the occurrence of the string x in the string s.
def strstr(s,x):
    N = len(s)
    M = len(x)
    i = 0
    while i <= N - M:
        j = 0 
        while j < M:
            if s[i+j] != x[j]:
                break
            j+=1
        if j==M:
            return i
        i+=1
    return -1
            
