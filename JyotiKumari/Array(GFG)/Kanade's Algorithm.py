class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        max_sum = arr[0]
        curr_sum = 0
        for element in arr:
            curr_sum+= element
            if(max_sum<curr_sum):
                max_sum = curr_sum
            if(curr_sum<0):
                curr_sum = 0
        return max_sum