class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	dup = [0]*n
    	elements = []
    	
    	for i in range(n):
    	    dup[arr[i]]+=1
    	for i in range(n):
    	    if dup[i] > 1:
    	        elements.append(i)
    	if len(elements) == 0:
    	    return [-1]
    	return elements
    	    
    	
    	    

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends