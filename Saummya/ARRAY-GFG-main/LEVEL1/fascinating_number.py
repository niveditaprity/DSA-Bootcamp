class Solution:

	def fascinating(self,n):
	    # code here
	    
	        
	        a=n*2
	        b=n*3
	        n2=str(a)+str(b)+str(n)
	        l=list(n2)
	        l.sort()
	        sum=""
	        for i in l:
	            sum=sum+i
	        if(sum=="123456789"):
	            return True
	        else:
	            return False
	   
