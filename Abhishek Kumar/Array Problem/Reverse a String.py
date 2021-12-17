#User function Template for python3

def reverseWord(s):
    #your code here
    s = list(s)
    length = len(s)
    for i in range(length//2):
        temp = s[i]
        s[i] = s[length-1-i]
        s[length-1-i] = temp
    return "".join(s)
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends