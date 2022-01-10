class Solution:

	def immediateSmaller(self,arr,n):
		# code here
		
		for i in range(1,n):
            if arr[i-1]> arr[i]:
                arr[i-1] = arr[i]
            else:
                arr[i-1] = -1
        arr[-1]= -1
        return arr
