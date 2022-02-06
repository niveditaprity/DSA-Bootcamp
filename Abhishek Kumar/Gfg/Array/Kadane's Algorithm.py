    def maxSubArraySum(self,arr,N):
        ##Your code here
        max_sum = arr[0]
        curr_sum = arr[0]
        
        for i in range(1,N):
            curr_sum = max(curr_sum + arr[i],arr[i])
            
            if curr_sum > max_sum:
                max_sum = curr_sum
                
        return max_sum
