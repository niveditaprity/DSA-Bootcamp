class Solution:
    def ValidPair(self, a, n): 
    	# Your code goes here
    	ans = 0
    	front=0
    	tail = n-1
    	a.sort()
    	while(front<tail):
    	    if(a[tail]+a[front]>0):
    	        ans+=(tail-front)
    	        tail-=1
    	    else:
    	        front+=1
    	    
        return ans