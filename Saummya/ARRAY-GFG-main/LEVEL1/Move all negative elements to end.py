
class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        temp = [0 for k in range(n)] 
        j = 0 # index of temp 
        for i in range(n): 
            if (arr[i] >= 0 ): 
                temp[j] = arr[i] 
                j +=1
        if (j == n or j == 0): 
            return
        for i in range(n): 
            if (arr[i] < 0): 
                temp[j] = arr[i] 
                j +=1
        for k in range(n): 
            arr[k] = temp[k] 
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends
