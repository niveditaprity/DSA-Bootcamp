#User function Template for python3

class Solution:
    # Function to find largest and second largest element in the array
    def largestAndSecondLargest(self, sizeOfArray, arr):
        res = -1
        larg = arr[0]
        for i in range(1,sizeOfArray):
            if arr[i] > larg:
                res = larg
                larg = arr[i]
            elif arr[i] < larg:
                if arr[i] > res:
                    res = arr[i]
        return [larg,res]


#{ 
#  Driver Code Starts
#Initial Template for Python 3


#Initial Template for Python 3

# Driver Code
def main():
    
    # testcase input
    testcases = int(input())
    
    # looping through all testcases
    while testcases > 0:
        
        sizeOfArray = int(input())
        
        arr = [int(x) for x in input().split()]
        
        li = Solution().largestAndSecondLargest(sizeOfArray, arr)
        for val in li:
            print(val, end = ' ')
        print('')
            
        testcases -= 1


if __name__ == '__main__':
    main()
# } Driver Code Ends