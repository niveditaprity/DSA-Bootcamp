# Your task is to complete this function
# Function should return True/False or 1/0
def PalinArray(arr ,n):
    
   c = 0
    for num in arr:
        
        if num == int(str(num)[::-1]):
            c += 1
    if c == len(arr):
        return 1
    else:
        return 0

#{ 
#  Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends
