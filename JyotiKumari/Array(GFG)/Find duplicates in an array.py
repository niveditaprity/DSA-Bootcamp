class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	d = {}
    	l = []
    	for element in arr:
    	    d[element]=0
    	
    	for element in arr:
    	    d[element]+=1
    	if(len(d)==n):
    	    l.append(-1)
    	else:
        	for key in d:
                if(d[key]>1):
    	            l.append(key)
    	l.sort()
    	return l 