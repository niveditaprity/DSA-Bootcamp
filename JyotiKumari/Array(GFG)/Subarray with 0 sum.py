class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        s = set()
        curr_sum = 0
        for element in arr:
            curr_sum+=element
            if(curr_sum==0 or curr_sum in s):
                return True
            s.add(curr_sum)
        return False